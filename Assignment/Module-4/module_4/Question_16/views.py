from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Appointment, Transaction
from Question_15.models import Doctor
from .utils import PaytmChecksum
import uuid

def book_appointment(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    if request.method == "POST":
        patient_name = request.POST.get('patient_name')
        fee = 500.00 # Placeholder fee
        appointment = Appointment.objects.create(
            doctor=doctor,
            patient_name=patient_name,
            fee=fee
        )
        return redirect('initiate_payment', appointment_id=appointment.id)
    return render(request, 'Question_16/book.html', {'doctor': doctor})

def initiate_payment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    order_id = str(uuid.uuid4())
    
    transaction = Transaction.objects.create(
        appointment=appointment,
        order_id=order_id,
        amount=appointment.fee
    )

    paytm_params = {
        "MID": settings.PAYTM_MERCHANT_ID,
        "ORDER_ID": order_id,
        "CUST_ID": str(appointment.id),
        "TXN_AMOUNT": str(appointment.fee),
        "CALLBACK_URL": settings.PAYTM_CALLBACK_URL,
    }

    checksum = PaytmChecksum.generateSignature(paytm_params, settings.PAYTM_MERCHANT_KEY)
    paytm_params["CHECKSUMHASH"] = checksum

    # Use a local mock checkout URL while Paytm servers are down
    mock_url = '/q16/mock-checkout/'
    
    return render(request, 'Question_16/paytm_form.html', {
        'paytm_params': paytm_params,
        'paytm_url': mock_url
    })

@csrf_exempt
def payment_callback(request):
    if request.method == "POST":
        paytm_params = {}
        checksum = None
        for key, value in request.POST.items():
            if key == 'CHECKSUMHASH':
                checksum = value
            elif key != 'csrfmiddlewaretoken': # Exclude CSRF token from signature calculation
                paytm_params[key] = value

        if not checksum:
            return render(request, 'Question_16/status.html', {
                'status': 'MISSING CHECKSUM',
                'received_keys': list(request.POST.keys()),
                'message': request.POST.get('RESPMSG', 'No message provided')
            })

        is_valid_checksum = PaytmChecksum.verifySignature(paytm_params, settings.PAYTM_MERCHANT_KEY, checksum)

        if is_valid_checksum:
            order_id = paytm_params.get('ORDERID') or paytm_params.get('ORDER_ID')
            transaction = get_object_or_404(Transaction, order_id=order_id)
            
            resp_code = paytm_params.get('RESPCODE')
            if resp_code == '01': # Success
                transaction.status = 'SUCCESS'
                transaction.transaction_id = paytm_params.get('TXNID')
                appointment = transaction.appointment
                appointment.paid = True
                appointment.save()
            else:
                transaction.status = 'FAILURE'
            
            transaction.save()
            return render(request, 'Question_16/status.html', {
                'status': transaction.status,
                'transaction': transaction,
                'message': paytm_params.get('RESPMSG')
            })
        else:
            return render(request, 'Question_16/status.html', {
                'status': 'CHECKSUM ERROR',
                'message': 'Security verification failed.'
            })
    
    return redirect('/')

@csrf_exempt
def mock_checkout(request):
    """
    A view that mimics the Paytm payment page.
    """
    if request.method == "POST":
        params = request.POST.dict()
        order_id = params.get('ORDER_ID')
        transaction = get_object_or_404(Transaction, order_id=order_id)
        
        # Prepare base parameters
        base_params = {
            "MID": params.get('MID'),
            "ORDERID": order_id,
            "TXNAMOUNT": params.get('TXN_AMOUNT'), # Corrected key
            "CURRENCY": "INR",
            "TXNID": "MOCK_TXN_889911",
            "BANKTXNID": "BANK_778899",
        }
        
        # 1. Success Params & Checksum
        success_params = base_params.copy()
        success_params.update({"STATUS": "TXN_SUCCESS", "RESPCODE": "01", "RESPMSG": "Txn Success"})
        success_checksum = PaytmChecksum.generateSignature(success_params, settings.PAYTM_MERCHANT_KEY)
        
        # 2. Failure Params & Checksum
        failure_params = base_params.copy()
        failure_params.update({"STATUS": "TXN_FAILURE", "RESPCODE": "02", "RESPMSG": "Payment Failed"})
        failure_checksum = PaytmChecksum.generateSignature(failure_params, settings.PAYTM_MERCHANT_KEY)

        return render(request, 'Question_16/mock_checkout.html', {
            'success_params': success_params,
            'success_checksum': success_checksum,
            'failure_params': failure_params,
            'failure_checksum': failure_checksum,
            'transaction': transaction
        })
    return redirect('/')
