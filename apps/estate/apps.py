from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class EstateConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.estate'
    verbose_name = _("4. Estate")

    def ready(self):
        from apps.estate import signals
