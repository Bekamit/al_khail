from django.db import models
from apps.staticdata.models import Form


class CatalogDownloader(models.Model):
    form = Form.objects.first()
    ROLES = (
        ('', form.role),
        ('agent', form.agent),
        ('buyer', form.buyer),
        ('explorer', form.exploring)
    )
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=100, verbose_name='E-mail')
    role = models.CharField(max_length=30, choices=ROLES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @staticmethod
    def create_loader(data: dict):
        return CatalogDownloader.objects.create(**data)
