from django.db import models
from django.utils.translation import gettext_lazy as _



class Facilities(models.Model):
    type = models.CharField(unique=True, max_length=50, verbose_name='Type of facilities')

    def icon_upload(self, filename):
        return f'facilities/{self.type_en}/{filename}'

    icon = models.ImageField(upload_to=icon_upload, null=True, blank=True, verbose_name='Icon path')

    def __str__(self):
        return self.type

    class Meta:
        app_label = 'project'
        verbose_name = _('Facilities Type')
        verbose_name_plural = _('Facilities Types')


class Project(models.Model):
    """
    ProjectModel():
    collection of Estate Projects objects
    add/edit/delete by administrator
    """
    name = models.CharField(max_length=100, verbose_name='Project name [En]', unique=True)
    facilities = models.ManyToManyField(to=Facilities, verbose_name='Project facilities', related_name='project')
    location = models.CharField(max_length=100, verbose_name='Location [En]')
    developer = models.CharField(null=True, blank=True, max_length=100, verbose_name='Developer [En]')
    completion = models.DateField(null=True, blank=True, verbose_name='Completion date')
    is_furnished = models.BooleanField(verbose_name='With furniture')

    def project_upload(self, filename):
        name = '_'.join(self.name.split())
        return f'catalog/{name}/{filename}'

    pdf_catalog = models.FileField(upload_to=project_upload, verbose_name='PDF catalog path')

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')


    def __str__(self):
        return self.name
