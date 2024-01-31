from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.city.models import City
from apps.project.models import Project

from django.db import models
from django.db.models import F
from django.utils.translation import gettext_lazy as _

import random


class EstateType(models.Model):
    """
    EstateTypeModel(MultilanguageModel):
    collection of types Real Estate objects
    exp: en: ['apartment', 'commercial', 'residents', ...]
    add/edit/delete by administrator
    """
    type = models.CharField(max_length=30, verbose_name='Estate Type', unique=True)

    class Meta:
        verbose_name = _('Estate Type')
        verbose_name_plural = _('Estate Types')

    def __str__(self):
        return self.type


class Estate(models.Model):
    """
    EstateModel(MultilanguageModel):
    collection of property characteristics Real Estate object
    add/edit/delete by administrator
    """
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, related_name='estate', verbose_name='Project')
    title = models.CharField(max_length=100, verbose_name='Title')
    area = models.FloatField(verbose_name='Area (m²)')
    description = models.TextField(max_length=1000, verbose_name='Description')
    price_usd = models.FloatField(verbose_name='Price at ($)')
    estate_type = models.ForeignKey(to=EstateType, on_delete=models.DO_NOTHING, related_name='estate')
    city = models.ForeignKey(to=City, on_delete=models.DO_NOTHING, related_name='estate')
    is_secondary = models.BooleanField(default=False, verbose_name='Secondary estate')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Create date')
    visits = models.IntegerField(default=0, verbose_name='Visits')

    class Meta:
        verbose_name = _('Estate')
        verbose_name_plural = _('Estates')
        ordering = ['price_usd',]

    def __str__(self):
        return f'{self.pk}: {self.title}'

    @staticmethod
    def is_valid(estate_id):
        return Estate.objects.filter(id=estate_id).exists()

    def visits_counter(self):
        self.visits = models.F('visits') + 1
        self.save(update_fields=['visits'])


class EstateImage(models.Model):
    """
    EstateImageModel:
    collection of photos and previews of Real Estate objects
    exp: ru/en/ar/tr: ['/back_media/estate/Antalia/6/photo1701607231.jpeg', ...]
    add/edit/delete by administrator
    """
    estate = models.ForeignKey(to=Estate, on_delete=models.CASCADE, related_name='images')

    def upload_to(self, filename):
        return f'estate/{self.estate.city.city_name_en}/{self.estate.id}/{filename}'

    img = models.ImageField(upload_to=upload_to)

    def __str__(self):
        return self.img.url
