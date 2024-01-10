from django.db import models
from apps.estate.models import Estate


class Appeal(models.Model):
    """
        Модель для оформления заявки на звонок на покупку/продажу обьекта недвижимости
    """

    is_for_purchase = models.BooleanField(default=True, verbose_name='Want to buy')
    estate_id = models.ForeignKey(Estate, on_delete=models.CASCADE, related_name='appel', null=True)
    name = models.CharField(max_length=70, verbose_name='Name')
    last_name = models.CharField(max_length=70, verbose_name='Last_name', blank=True, null=True)
    phone = models.CharField(max_length=70, verbose_name='Phone number')
    lang = models.CharField(max_length=30, verbose_name='Message Language')
    at_time = models.DateTimeField(verbose_name='Call at time', null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Send date')

    class Meta:
        verbose_name = 'Message from site'
        verbose_name_plural = 'Messages from site'

    def __str__(self):
        return f'{self.created_at.strftime("%Y-%m-%d, %H:%M")}  {self.name} for {"BUY" if self.is_for_purchase else "SELL"}'
