from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_registration_email(user_email):
    subject = 'Welcome to Our Platform!'
    message = 'Thank you for registering with us.'
    send_mail(subject, message, settings.EMAIL_HOST_USER, [user_email], fail_silently=False) 