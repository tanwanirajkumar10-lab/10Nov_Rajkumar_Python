import requests
import json
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.conf import settings

from .forms import UserRegistrationForm

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_email = user.email
            send_confirmation_email(user.username, user_email)
            
            request.session['reg_user'] = user.username
            request.session['reg_email'] = user_email
            return redirect('Question_19:registration-success')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'Question_19/register.html', {'form': form})

def registration_success_view(request):
    username = request.session.get('reg_user', 'User')
    email = request.session.get('reg_email', 'unknown@email.com')
    api_key = getattr(settings, 'SENDGRID_API_KEY', 'your_sendgrid_api_key_here')
    from_email = getattr(settings, 'SENDGRID_FROM_EMAIL', 'verified@email.com')

    return render(request, 'Question_19/success.html', {
        'username': username,
        'email': email,
        'is_simulated': api_key == 'your_sendgrid_api_key_here',
        'from_email': from_email
    })

def send_confirmation_email(username, user_email):
    api_key = getattr(settings, 'SENDGRID_API_KEY', 'your_sendgrid_api_key_here')
    from_email = getattr(settings, 'SENDGRID_FROM_EMAIL', 'verified@email.com')
    
    subject = "Welcome to tech world !"
    content = f"Hello {username},\n\nWelcome to tech world ! Your registration was successful.\nWe are excited to have you on board.\n\nBest regards,\nThe Question 19 Team"

    if api_key == 'your_sendgrid_api_key_here':
        # Simulator Mode
        print("\n--- SENDGRID SIMULATION ---")
        print(f"To: {user_email}")
        print(f"From: {from_email}")
        print(f"Subject: {subject}")
        print(f"Body: {content}")
        print("---------------------------\n")
    else:
        # Live Mode (REST API v3)
        url = "https://api.sendgrid.com/v3/mail/send"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "personalizations": [{"to": [{"email": user_email}]}],
            "from": {"email": from_email},
            "subject": subject,
            "content": [{"type": "text/plain", "value": content}]
        }
        try:
            response = requests.post(url, headers=headers, json=data)
            if response.status_code >= 400:
                print(f"SendGrid API Error ({response.status_code}): {response.text}")
            else:
                print(f"SendGrid Email Sent Successfully (Status {response.status_code})")
        except Exception as e:
            print(f"Connection Error while sending to SendGrid: {e}")
