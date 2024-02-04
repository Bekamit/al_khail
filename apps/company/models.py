from django.db import models
from django.utils.translation import gettext_lazy as _
from solo.models import SingletonModel


class Company(SingletonModel):
    company_name = models.CharField(max_length=50, verbose_name='Company name')
    about = models.TextField(verbose_name='About company')
    phone = models.CharField(max_length=150, verbose_name='Phone number')
    email = models.EmailField(verbose_name='E-mail')
    company_img = models.ImageField(upload_to='company/', verbose_name='Company photo path')
    # contact_person = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = _('About company')

    def __str__(self):
        return self.company_name
