from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.estate.models import Estate


class CatalogDownloader(models.Model):
    """
       Модель для получения данных от пользователей, скачивающих PDF каталог проекта
    """
    name = models.CharField(max_length=50, verbose_name='Name')
    email = models.EmailField(verbose_name='E-mail')
    phone = models.CharField(max_length=100, verbose_name='Phone number', null=True)
    role = models.CharField(max_length=30, verbose_name='Role')
    created_at = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=100, verbose_name='City')

    class Meta:
        verbose_name = _('Catalog downloader')
        verbose_name_plural = _('Catalog downloaders')

    def __str__(self):
        return self.name

    @staticmethod
    def create_downloader(data: dict):
        return CatalogDownloader.objects.create(**data)


class Appeal(models.Model):
    """
        Модель для оформления заявки на звонок на покупку/продажу/консультацию по обьекту недвижимости
    """
    CHOICES = [
        ('buy', 'buy'),
        ('sell', 'sell'),
        ('consultation', 'consultation'),
    ]
    appeal_type = models.CharField(max_length=20, choices=CHOICES, verbose_name='Type of Appeal')
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE, related_name='appeals', null=True)
    name = models.CharField(max_length=70, verbose_name='Name')
    phone = models.CharField(max_length=70, verbose_name='Phone number')
    lang = models.CharField(max_length=30, verbose_name='Message Language', blank=True)
    city = models.CharField(max_length=100, verbose_name='Respondent city')
    at_date = models.DateField(verbose_name='Call in date', null=True, blank=True)
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
