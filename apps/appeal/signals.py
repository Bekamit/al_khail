from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Appeal
from .tasks import send_appeal_email_task


@receiver(post_save, sender=Appeal)
def send_appeal_email1(sender, instance, **kwargs):
    if kwargs.get('created',False):

        subject = 'Test'
        message = f'Your verification code is: {instance.id}'
        sender_email = 'sayansenedwne@gmail.com'
        recipient_email = 'ramzhan8@gmail.com'

        send_mail(subject, message, sender_email, [recipient_email], fail_silently=False)