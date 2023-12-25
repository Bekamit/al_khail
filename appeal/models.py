from django.db import models
from rest_framework.response import Response


class AppealType(models.Model):
    appeal_type = models.CharField(max_length=70)


class Appeal(models.Model):
    """
        Модель для клиента, для оформления заявки на обратную связь
    """

    # estate_page_id = models.ForeignKey(EstatePage, on_delete=models.CASCADE, related_name='estate_page')
    # appeal_type_id = models.ForeignKey(AppealType, on_delete=models.CASCADE, related_name='type')
    name = models.CharField(max_length=70)
    phone = models.CharField(max_length=70)
    lang = models.CharField(max_length=30)
    at_time = models.DateTimeField()
    more_about_time = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now=True)
