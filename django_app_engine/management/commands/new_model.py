"""
Login to API Manager

COMMIT_MSG_ENTRY: add management command to login to API Manager

"""

from django.core.management.templates import TemplateCommand
from django.core.management import BaseCommand
from pathlib import Path
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy as _lazy
from django.utils import translation
import os

MANAGEMENT_BASE_DIR = Path(__file__).resolve().parent.parent


class Command(BaseCommand):
    help = _("Model API Manager")

    def handle(self, **options):
        print(MANAGEMENT_BASE_DIR)
        if os.path.exists(
            os.path.join(MANAGEMENT_BASE_DIR, "default_app_model_template")
        ):
            print(MANAGEMENT_BASE_DIR)
