from django.db.models.signals import post_init
from django.dispatch import receiver
from .models import Estate


@receiver(post_init, sender=Estate)
def estate_visits_counter(instance: Estate, **kwargs):
    instance.visits_counter()

