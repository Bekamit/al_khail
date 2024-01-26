from django.db import models


class CatalogDownloader(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    email = models.EmailField(verbose_name='E-mail')
    phone = models.CharField(max_length=100, verbose_name='Phone number')
    role = models.CharField(max_length=30, verbose_name='Role')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @staticmethod
    def create_loader(data: dict):
        return CatalogDownloader.objects.create(**data)
