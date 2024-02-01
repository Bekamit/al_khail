from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class StaticdataConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.staticdata'
    verbose_name = _('7. Static content')
