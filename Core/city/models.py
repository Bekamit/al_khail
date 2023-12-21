from django.db import models

class City(models.Model):
    """
    CityModel(MultilanguageModel):
    collection of cities where real estate properties are located
    exp: en: ['Antalia', 'Resort town in Turkey', 'preview_image.jpeg']
    add/edit/delete by administrator
    """
    city_name = models.CharField(max_length=255)
    city_description = models.TextField()

    def upload_to(self, filename):
        return f'cities/{self.city_name_en}/{filename}'

    city_img = models.ImageField(upload_to=upload_to)

    def __str__(self):
        return self.city_name