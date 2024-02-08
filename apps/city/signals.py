import os
import shutil

from django.db.models.signals import pre_delete
from django.dispatch import receiver

from core.settings.base import MEDIA_ROOT
from apps.estate.models import City


@receiver(pre_delete, sender=City)
def delete_image_files(instance: City, **kwargs):
    if hasattr(instance, 'city_img'):
        try:
            tree = os.path.join(MEDIA_ROOT, os.path.dirname(instance.city_img.path))
            shutil.rmtree(tree, ignore_errors=False)
        except FileNotFoundError as e:
            print(e)
