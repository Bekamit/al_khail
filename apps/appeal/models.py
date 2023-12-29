from django.db import models
from apps.estate.models import Estate


class Appeal(models.Model):
    """
        Модель для оформления заявки на звонок на покупку/продажу обьекта недвижимости
    """

    is_for_purchase = models.BooleanField(default=True)
    estate_id = models.ForeignKey(Estate, on_delete=models.CASCADE, related_name='appel')
    name = models.CharField(max_length=70)
    phone = models.CharField(max_length=70)
    lang = models.CharField(max_length=30)
    at_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
