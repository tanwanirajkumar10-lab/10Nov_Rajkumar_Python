import os
from twilio.rest import Client
from django.conf import settings

def send_otp_via_twilio(mobile_number, otp):
    """
    Sends an OTP to the given mobile number using Twilio.
    Falls back to console printing if credentials are placeholders.
    """
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    twilio_number = settings.TWILIO_PHONE_NUMBER

    message_body = f"Your Verification Code is: {otp}"

    if account_sid == 'your_account_sid' or auth_token == 'your_auth_token':
        print("\n" + "="*50)
        print(f"SIMULATED SMS to {mobile_number}: {message_body}")
        print("Reason: Twilio credentials not configured in settings.py")
        print("="*50 + "\n")
        return True

    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=message_body,
            from_=twilio_number,
            to=mobile_number
        )
        return True
    except Exception as e:
        print(f"Error sending SMS via Twilio: {e}")
        return False
        
