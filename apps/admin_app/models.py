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
    is_superuser = models.BooleanField(_('superuser status'), default=False)
    language = models.CharField(max_length=10, choices=CHOICES, default='en')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def is_active(self):
        return self.is_superuser

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')