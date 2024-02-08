from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CityConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.city'
    verbose_name = _("5. City")

    def ready(self):
        import apps.city.signals
