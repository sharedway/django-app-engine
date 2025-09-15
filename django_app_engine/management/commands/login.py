"""
Login to API Manager

COMMIT_MSG_ENTRY: add management command to login to API Manager

"""

from django.core.management.templates import TemplateCommand
from django.core.management import BaseCommand
from pathlib import Path
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy as _lazy
from django.utils import translation


class Command(BaseCommand):
    help = _("Login to api Manager")

    def handle(self, **options):
        pass
