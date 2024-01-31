from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AdminAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.admin_app'
    verbose_name = _("1. Settings")
