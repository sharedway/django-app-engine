from django.apps import AppConfig


class DjangoAppEngineConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "django_app_engine"

    def ready(self):
        super().ready()
        import django_app_engine.models
        import django_app_engine.signals
        import django_app_engine.tasks
