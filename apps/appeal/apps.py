from django.apps import AppConfig


class AppealConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.appeal'

    def ready(self):
        from . import signals
