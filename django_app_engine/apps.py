from django.apps import AppConfig


class DjangoAppEngineConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "django_app_engine"

    @property
    def APP_VERSION(self):

        _app_version = "0.0.1"
        with open("django_app_engine/app_version.txt") as app_version_file:
            _app_version = app_version_file.read()
        return _app_version

    def ready(self):
        super().ready()
        import django_app_engine.models
        import django_app_engine.signals
        import django_app_engine.tasks
