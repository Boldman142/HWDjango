from django.core.mail import send_mail

from config import settings


def send(topic, text, to):
    send_mail(
        subject=topic,
        message=text,
        recipient_list=to,
        from_email=settings.EMAIL_HOST_USER
    )
