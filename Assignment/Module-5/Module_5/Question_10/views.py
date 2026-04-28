from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import random
from .models import UserOTP
from .utils import send_otp_via_twilio

def login_view(request):
    return render(request, 'Question_10/login.html')

@login_required
def process_otp(request):
    """
    Step 1: Check if mobile number is provided. If not, show a form.
    If provided, send OTP.
    """
    if request.method == 'POST':
        mobile_number = request.POST.get('mobile_number')
        otp = str(random.randint(100000, 999999))
        
        # Save or update OTP
        user_otp, created = UserOTP.objects.get_or_create(user=request.user)
        user_otp.mobile_number = mobile_number
        user_otp.otp = otp
        user_otp.save()
        
        # Send via Twilio
        if send_otp_via_twilio(mobile_number, otp):
            messages.success(request, f"OTP sent to {mobile_number}")
            return redirect('verify-otp')
        else:
            messages.error(request, "Failed to send OTP. Please try again.")
            
    return render(request, 'Question_10/initiate_otp.html')

@login_required
def verify_otp(request):
    """
    Step 2: Enter and verify the 6-digit code.
    """
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        try:
            user_otp = UserOTP.objects.get(user=request.user)
            if user_otp.otp == entered_otp:
                # Success!
                request.session['otp_verified'] = True
                return redirect('success-page')
            else:
                messages.error(request, "Invalid OTP. Please try again.")
        except UserOTP.DoesNotExist:
            return redirect('process-otp')

    return render(request, 'Question_10/verify_otp.html')

@login_required
def success_view(request):
    if not request.session.get('otp_verified'):
        return redirect('verify-otp')
    return render(request, 'Question_10/success.html')
