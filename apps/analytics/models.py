from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.estate.models import Estate


class DownloadCatalog(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    phone_number = models.IntegerField(blank=True, null=True)
    email = models.EmailField()
    role = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def create_analytics(data: dict):
        return DownloadCatalog.objects.create(**data)




class CatalogDownloader(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    email = models.EmailField(verbose_name='E-mail')
    phone = models.CharField(max_length=100, verbose_name='Phone number')
    role = models.CharField(max_length=30, verbose_name='Role')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Catalog downloader')
        verbose_name_plural = _('Catalog downloaders')

    def __str__(self):
        return self.name

    @staticmethod
    def create_loader(data: dict):
        return CatalogDownloader.objects.create(**data)


class Appeal(models.Model):
    """
        Модель для оформления заявки на звонок на покупку/продажу обьекта недвижимости
    """

    is_for_purchase = models.BooleanField(verbose_name='Want to buy')
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE, related_name='appel', null=True)
    name = models.CharField(max_length=70, verbose_name='Name')
    phone = models.CharField(max_length=70, verbose_name='Phone number')
    lang = models.CharField(max_length=30, verbose_name='Message Language')
    at_time = models.DateTimeField(verbose_name='Call at time', null=True)
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Send date')
    is_send = models.BooleanField(default=True, verbose_name='Send letter')

    class Meta:
        verbose_name = _('Message from site')
        verbose_name_plural = _('Messages from site')

    def __str__(self):
        return f'{self.pk}'

    @staticmethod
    def create_appeal(data: dict):
        return Appeal.objects.create(**data)

    def send_error(self):
        self.is_send = False
        self.save()
