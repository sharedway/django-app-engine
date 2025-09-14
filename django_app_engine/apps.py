from django.apps import AppConfig


class DjangoAppEngineConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "django_app_engine"

    def ready(self):
        super().ready()
        import models
        import signals
        import tasks
