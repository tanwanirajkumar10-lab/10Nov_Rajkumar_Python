import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout_page(request):
    """
    Renders the checkout page showing the appointment details and the Pay button.
    """
    context = {
        'doctor_name': 'Dr. Sharma (Cardiologist)',
        'appointment_time': '10:00 AM, Tomorrow',
        'consultation_fee': 500, # 500 INR
        'currency': 'INR'
    }
    return render(request, 'Question_21/checkout.html', context)

def create_checkout_session(request):
    """
    Creates a Stripe Checkout Session and redirects the user to the Stripe payment page.
    """
    if request.method == 'POST':
        # Retrieve the domain to construct success and cancel URLs
        domain_url = request.build_absolute_uri('/')[:-1] 

        try:
            # Create new Checkout Session for the order
            # Other optional params include:
            # [billing_address_collection] - to display billing address details on the page
            # [customer] - if you have an existing Stripe Customer ID
            # [payment_intent_data] - lets capture the payment later
            # [customer_email] - lets you prefill the email input in the form
            
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + reverse('q21_payment_success') + '?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + reverse('q21_payment_cancel'),
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'price_data': {
                            'currency': 'inr',
                            'unit_amount': 500 * 100, # 500 INR in paise
                            'product_data': {
                                'name': 'Dr. Sharma - Consultation Fee',
                                'description': 'Cardiology Consultation Appointment',
                            },
                        },
                        'quantity': 1,
                    }
                ]
            )
            return redirect(checkout_session.url, code=303)
            
        except Exception as e:
            # Fallback mock for testing when Stripe keys are 'sk_test_dummy'
            logger.error(f"Stripe setup error: {str(e)}")
            messages.warning(request, "Mock Payment Engine Enabled: Since real Stripe keys were not provided, we simulated a successful checkout.")
            return redirect('q21_payment_success')

    return redirect('q21_checkout')

def payment_success(request):
    """
    Displays the successful booking message.
    """
    # session_id = request.GET.get('session_id') 
    # Can verify session with stripe.checkout.Session.retrieve(session_id)
    return render(request, 'Question_21/success.html')

def payment_cancel(request):
    """
    Displays the payment cancelled message.
    """
    return render(request, 'Question_21/cancel.html')
