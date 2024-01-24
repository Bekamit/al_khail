from decouple import config
from core.celery import celery_app
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages

from .models import Appeal
import config


@celery_app.task
def send_appeal_email_task(appeal_id):
    try:
        instance = Appeal.objects.get(pk=appeal_id)
        subject = 'Al-Khail'

        html_message = render_to_string('appeal_template.html', {'instance': instance})

        from_email = config('DEFAULT_FROM_EMAIL')
        recipient_list = [str(config.ADMIN_EMAIL)]

        email = EmailMessage(
            subject,
            html_message,
            from_email,
            recipient_list
        )
        email.content_subtype = 'html'

        email.send()
    except Appeal.DoesNotExist:
        if instance:
            instance.send_error()
            messages.error(instance, 'The email cannot be send')
