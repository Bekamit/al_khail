from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ProjectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.project'
    verbose_name = _("3. Project")

    def ready(self):
        import apps.project.signals
