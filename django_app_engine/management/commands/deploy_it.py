from django.core.management.templates import TemplateCommand
from django.core.management import BaseCommand
from pathlib import Path
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy as _lazy
from django.utils import translation

MANAGEMENT_BASE_DIR = Path(__file__).resolve().parent.parent


class Command(BaseCommand):
    help = _("Deploy this project to the mesh")

    def handle(self, **options):
        print(MANAGEMENT_BASE_DIR)
