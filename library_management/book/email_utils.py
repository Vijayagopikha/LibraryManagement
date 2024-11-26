from django.core.mail import send_mail
from django.conf import settings

def send_email(subject, message, recipient_email):
    """
    Function to send an email to the user.
    """
    try:
        send_mail(
            subject,                  # Subject of the email
            message,                  # Body of the email
            settings.EMAIL_HOST_USER,  # Sender email from settings
            [recipient_email],        # Recipient's email
            fail_silently=False,      # If set to False, will raise exceptions on errors
        )
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False
