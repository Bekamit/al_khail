from django.db import models
from django.utils.translation import gettext_lazy as _


class City(models.Model):
    """
    CityModel(MultilanguageModel):
    collection of cities where real estate properties are located
    exp: en: ['Antalia', 'Resort town in Turkey', 'preview_image.jpeg']
    add/edit/delete by administrator
    """
    city_name = models.CharField(max_length=255, verbose_name='City', unique=True)
    city_description = models.TextField(verbose_name='City descriptions')

    def upload_to(self, filename):
        filename = '_'.join(filename.split())
        city = self.city_name_en.replace(' ', '_')
        return f'cities/{city}/{filename}'

    city_img = models.ImageField(upload_to=upload_to, verbose_name='City photo path')

    class Meta:
        verbose_name_plural = _('Cities')

    def __str__(self):
        return self.city_name
