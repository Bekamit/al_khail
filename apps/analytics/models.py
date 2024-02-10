from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.estate.models import Estate


class CatalogDownloader(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    email = models.EmailField(verbose_name='E-mail')
    phone = models.CharField(max_length=100, verbose_name='Phone number')
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
        Модель для оформления заявки на звонок на покупку/продажу обьекта недвижимости
        Model for requesting a call to buy/sell a real estate object
    """

    is_for_purchase = models.BooleanField(verbose_name='Want to buy')
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE, related_name='appel', null=True)
    name = models.CharField(max_length=70, verbose_name='Name')
    phone = models.CharField(max_length=70, verbose_name='Phone number')
    lang = models.CharField(max_length=30, verbose_name='Message Language')
    at_time = models.DateField(null=True)
    city = models.CharField(max_length=100)
    at_time = models.DateTimeField(verbose_name='Call at time', null=True)
    city = models.CharField(max_length=100, verbose_name='Respondent city')
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


class Consultation(models.Model):
    """
        Модель для формы с вопросами клиектов
        Model for form with extra questions
    """

    name = models.CharField(max_length=70, verbose_name='Name')
    phone = models.CharField(max_length=70, verbose_name='Phone number')
    city = models.CharField(max_length=100, verbose_name='City')
    at_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create_consultation(cls, **data):
        return cls.objects.create(**data)

    def __str__(self):
        return f'{self.pk} -- {self.name}'
