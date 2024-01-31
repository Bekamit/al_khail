from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser, PermissionsMixin):
    CHOICES = (
        ('en', _('English')),
        ('tr', _('Turkish')),
        ('ru', _('Russian')),
    )
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_('username'), max_length=30, default='manager')
    language = models.CharField(max_length=10, choices=CHOICES, default='en')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def has_perm(self, perm, obj=None):
        return True

    def __str__(self):
        return self.email

    # def get_email(self):
    #     return self.email
