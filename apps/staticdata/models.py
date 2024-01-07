from django.db import models
from solo.models import SingletonModel


class StaticData(SingletonModel):
    default_image = models.ImageField(upload_to='default_image/', verbose_name='default image path')
    field1 = models.CharField(max_length=100)
    field2 = models.TextField()

    def __str__(self):
        return 'static data'

    @staticmethod
    def default_img():
        return StaticData.objects.first().default_image

    class Meta:
        verbose_name = 'Static Data'
        verbose_name_plural = 'Static Data'
