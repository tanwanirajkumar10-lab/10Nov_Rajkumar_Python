import random
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from twilio.rest import Client
import logging

logger = logging.getLogger(__name__)

def register_with_otp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        mobile_number = request.POST.get('mobile_number')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('q20_register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('q20_register')
            
        # Generate 6-digit OTP
        otp = str(random.randint(100000, 999999))
        
        # Save info in session
        request.session['registration_data'] = {
            'username': username,
            'email': email,
            'password': password,
            'mobile_number': mobile_number,
            'otp': otp
        }
        
        # Send OTP via Twilio
        try:
            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
            message = client.messages.create(
                body=f"Your OTP for registration is: {otp}",
                from_=settings.TWILIO_PHONE_NUMBER,
                to=mobile_number
            )
            messages.success(request, f'OTP sent to {mobile_number}.')
        except Exception as e:
            # Fallback for testing without credentials
            error_msg = str(e)
            logger.error(f"Twilio error: {error_msg}")
            messages.warning(request, f'Twilio Error: {error_msg}. Using test OTP: {otp}')
            print(f"Fallback OTP for {username}: {otp}")

        return redirect('q20_verify_otp')

    return render(request, 'Question_20/register.html')

def verify_otp(request):
    if 'registration_data' not in request.session:
        messages.error(request, 'Session expired. Please register again.')
        return redirect('q20_register')

    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        session_data = request.session['registration_data']

        if entered_otp == session_data['otp']:
            # Create the user
            user = User.objects.create_user(
                username=session_data['username'],
                email=session_data['email'],
                password=session_data['password']
            )
            
            # Clean up session
            del request.session['registration_data']

            messages.success(request, 'Registration successful!')
            return redirect('home')  # Redirect back to module 5 dashboard
        else:
            messages.error(request, 'Invalid OTP. Please try again.')
            return redirect('q20_verify_otp')

    return render(request, 'Question_20/verify_otp.html')
