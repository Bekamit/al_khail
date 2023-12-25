from django.apps import AppConfig


class AppealConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appeal'

    def ready(self):
        import appeal.signals
