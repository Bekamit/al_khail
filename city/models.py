from django.db import models
from django.db.models import Q
from city.models import City


class EstateType(models.Model):
    """
    EstateTypeModel(MultilanguageModel):
    collection of types Real Estate objects
    exp: en: ['apartment', 'commercial', 'stead', 'residents']
    add/edit/delete by administrator
    """
    type = models.CharField(max_length=30)

    def __str__(self):
        return self.type

    @staticmethod
    def in_collection(estate_type: str) -> bool:
        query = (Q(type_en__icontains=estate_type) |
                 Q(type_ar__icontains=estate_type) |
                 Q(type_tr__icontains=estate_type) |
                 Q(type_ru__icontains=estate_type))
        return EstateType.objects.filter(query).exists()


class Estate(models.Model):
    """
    EstateModel(MultilanguageModel):
    collection of property characteristics Real Estate object
    exp: ru: ['1ая квартира', 'Монолит', '58.8', 'Ленинский', 'апартаменты', 'Бишкек', 'true', '2023-12-17T16:56:58']
    add/edit/delete by administrator
    """
    name = models.CharField(max_length=100, verbose_name='estate_name')
    developer = models.CharField(max_length=100, verbose_name='estate_developer')
    area = models.FloatField(verbose_name='estate_area')
    district = models.CharField(max_length=100, verbose_name='estate_district')
    description = models.TextField(max_length=500, verbose_name='estate_description')
    estate_type = models.ForeignKey(to=EstateType, on_delete=models.DO_NOTHING, related_name='estate')
    city = models.ForeignKey(to=City, on_delete=models.DO_NOTHING, related_name='estate')
    is_secondary = models.BooleanField(default=True, verbose_name='estate_is_secondary')

    # price = models.FloatField()
    # currency = models.CharField(max_length=4)

    def upload_to(self, filename):
        return f'catalog/{self.estate.city.city_name_en}/{filename}'

    # pdf_catalog = models.FileField(upload_to=upload_to)
    create_at = models.DateTimeField(auto_now_add=True)

    # update_at = models.DateTimeField(auto_now=True)
    # visits = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.pk}: {self.name}'

    @staticmethod
    def city_id_is_valid(city_id):
        return City.objects.filter(id=city_id).exists()

    @staticmethod
    def estate_type_id_is_valid(estate_type_id):
        return EstateType.objects.filter(id=estate_type_id).exists()


class EstateImage(models.Model):
    """
    EstateImageModel:
    collection of photographs and previews of Real Estate objects
    exp: ru/en/ar/tr: ['/media/estate/Antalia/6/photo1701607231.jpeg']
    add/edit/delete by administrator
    """
    estate = models.ForeignKey(to=Estate, on_delete=models.CASCADE, related_name='image')

    def upload_to(self, filename):
        return f'estate/{self.estate.city.city_name_en}/{self.estate.id}/{filename}'

    img = models.ImageField(upload_to=upload_to)

    def __str__(self):
        return self.img.url
