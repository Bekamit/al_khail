from core.celery import app
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from pathlib import Path
from django.conf import settings
from .models import Appeal
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent


@app.task
def send_appeal_email_task(appeal_id):
    try:
        instance = Appeal.objects.get(pk=appeal_id)
        subject = 'Al-Khail'

        html_message = render_to_string(f'{BASE_DIR}/apps/appeal/templates/appeal_template.html',
                                        {'instance': instance})

        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [str(config('ADMIN_EMAIL'))]

        email = EmailMessage(
            subject,
            html_message,
            from_email,
            recipient_list
        )
        email.content_subtype = 'html'

        email.send()
    except Appeal.DoesNotExist:
        pass
