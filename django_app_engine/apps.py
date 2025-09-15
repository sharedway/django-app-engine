from django.apps import AppConfig
from django.conf import settings
from django.core.checks import Critical, Error, Warning
from django.core.checks import register
from functools import partial


class AppRequirementsChecker:
    """
    COMMIT_MSG_ENTRY: add checker for required settings variables
    """

    def __init__(self, required_settings_entries={}, optional_settings_entries={}):
        self.required_settings_entries = required_settings_entries
        self.optional_settings_entries = optional_settings_entries
        self.errors = []

    def check_app_requirements(self, app_configs, **kwargs):
        """
        COMMIT_MSG_ENTRY: Add a msg to warn when a var is missing from settings
        """

        for k, v in self.optional_settings_entries.items():
            if not hasattr(settings, k):
                self.errors.append(
                    Warning(
                        f"{v}",
                        hint=f"Optional  {k} via .env or add to django.settings",
                        obj="app_constant checker",
                        id=f"not_found_{k}",
                    )
                )

        for k, v in self.required_settings_entries.items():
            if not hasattr(settings, k):
                self.errors.append(
                    Critical(
                        f"{v}",
                        hint=f"Configure  {k} via .env or add to django.settings",
                        obj="app_constant checker",
                        id=f"not_found_{k}",
                    )
                )
        return self.errors


class DjangoAppEngineConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "django_app_engine"

    REQUIRED_SETTINGS_ENTRIES = {}
    OPTIONAL_SETTINGS_ENTRIES = {}

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

        app_checker = AppRequirementsChecker(
            required_settings_entries=self.REQUIRED_SETTINGS_ENTRIES,
            optional_settings_entries=self.OPTIONAL_SETTINGS_ENTRIES,
        )
        bound_check = partial(app_checker.check_app_requirements)
        register(bound_check)
