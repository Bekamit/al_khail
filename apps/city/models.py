from django.db import models


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
        return f'cities/{self.city_name_en}/{filename}'

    city_img = models.ImageField(upload_to=upload_to, verbose_name='City photo path')

    class Meta:
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.city_name_en
