from django.db import models
from django.db.models import F

from apps.city.models import City
from apps.staticdata.models import StaticData


class EstateType(models.Model):
    """
    EstateTypeModel(MultilanguageModel):
    collection of types Real Estate objects
    exp: en: ['apartment', 'commercial', 'residents', ...]
    add/edit/delete by administrator
    """
    type = models.CharField(max_length=30, verbose_name='Estate Type')

    class Meta:
        verbose_name = 'Estate Type'
        verbose_name_plural = 'Estate Types'

    def __str__(self):
        return self.type


class Project(models.Model):
    """
    ProjectModel():
    collection of Estate Projects objects
    add/edit/delete by administrator
    """
    name = models.CharField(max_length=100, verbose_name='Project')

    def project_upload(self, filename):
        return f'catalog/{self.name}/{filename}'

    pdf_catalog = models.FileField(upload_to=project_upload, verbose_name='PDF catalog path')

    def __str__(self):
        return self.name


class Estate(models.Model):
    """
    EstateModel(MultilanguageModel):
    collection of property characteristics Real Estate object
    add/edit/delete by administrator
    """
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, related_name='estate', verbose_name='Project')
    title = models.CharField(max_length=100, verbose_name='Title')
    developer = models.CharField(max_length=100, verbose_name='Developer')
    district = models.CharField(max_length=100, verbose_name='District')
    area = models.FloatField(verbose_name='Area (m2)')
    description = models.TextField(max_length=500, verbose_name='Description')
    estate_type = models.ForeignKey(to=EstateType, on_delete=models.DO_NOTHING, related_name='estate')
    city = models.ForeignKey(to=City, on_delete=models.DO_NOTHING, related_name='estate')
    is_secondary = models.BooleanField(default=True, verbose_name='Secondary estate')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Create date')
    visits = models.IntegerField(default=0, verbose_name='Visits')

    def __str__(self):
        return f'{self.pk}: {self.title}'

    @staticmethod
    def get_estate_id(estate_id):
        return Estate.objects.filter(id=estate_id).exists()

    @property
    def default_img(self):
        img = StaticData.default_img()
        return img

    def visits_counter(self):
        self.visits = F('visits') + 1
        self.save(update_fields=['visits'])


class EstateImage(models.Model):
    """
    EstateImageModel:
    collection of photos and previews of Real Estate objects
    exp: ru/en/ar/tr: ['/back_media/estate/Antalia/6/photo1701607231.jpeg', ...]
    add/edit/delete by administrator
    """
    estate = models.ForeignKey(to=Estate, on_delete=models.CASCADE, related_name='image')

    def upload_to(self, filename):
        return f'estate/{self.estate.city.city_name_en}/{self.estate.id}/{filename}'

    img = models.ImageField(upload_to=upload_to)

    def __str__(self):
        return self.img.url
