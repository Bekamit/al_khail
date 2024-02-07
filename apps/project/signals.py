import os
import shutil

from django.db.models.signals import pre_delete
from django.dispatch import receiver

from core.settings.base import MEDIA_ROOT
from .models import Project


@receiver(pre_delete, sender=Project)
def delete_related_files(instance: Project, **kwargs):
    if hasattr(instance, 'pdf_catalog'):
        try:
            tree = os.path.join(MEDIA_ROOT, 'catalog', instance.name.replace(' ', '_'))
            shutil.rmtree(tree, ignore_errors=False)
        except FileNotFoundError as e:
            print(e)