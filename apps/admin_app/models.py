from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    CHOICES = (
        ('en', _('English')),
        ('tr', _('Turkish')),
        ('ru', _('Russian')),
    )

    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=100, unique=False, default='manager')
    password = models.CharField(max_length=128, verbose_name='password')
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active status'), default=True)
    language = models.CharField(max_length=10, choices=CHOICES, default='en')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
