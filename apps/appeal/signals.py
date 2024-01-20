from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Appeal
from .tasks import send_appeal_email_task


@receiver(post_save, sender=Appeal)
def send_appeal_email(sender, instance, created, **kwargs):
    if created:
        send_appeal_email_task(instance.id)  # delay was deleted for production testins
