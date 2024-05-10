from django.core.mail import send_mail
from django.conf import settings


def send_email(subject, message, to):
    try:
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, message, from_email, [to], fail_silently=False)
    except:
        pass