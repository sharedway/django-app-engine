from pathlib import Path
from typing import Any, Dict

from django.conf import settings
from django.core.management.commands.startapp import Command as UpstreamStartAppCommand
import os

MANAGEMENT_BASE_DIR = Path(__file__).resolve().parent.parent


def _as_str(v):
    # argparse defaults should be str/None/bool for these flags
    if isinstance(v, Path):
        return str(v)
    return v


class Command(UpstreamStartAppCommand):
    """
    Wrapper around Django's 'startapp' that applies project-wide default
    options from settings.STARTAPP_DEFAULTS (if present), while preserving
    the original behavior.

    Example settings:

    STARTAPP_DEFAULTS = {
        # same dest names as upstream options
        "directory": BASE_DIR / "apps",
        "template": BASE_DIR / "scaffolds" / "startapp_template",
        "extension": "py,txt",
        "name": "apps,models,views,urls,admin",
        "exclude": "tests.py,__pycache__",
        "noinput": True,  # behave as if you passed --no-input
    }
    """

    help = (
        "Start a new app (wrapper with customizable defaults from django_app_engine)."
    )

    def add_arguments(self, parser):
        # Let upstream define the full interface first
        super().add_arguments(parser)

        # Pull defaults from settings (optional)
        raw_defaults: Dict[str, Any] = getattr(settings, "STARTAPP_DEFAULTS", {}) or {}

        # Normalize types for argparse defaults
        normalized = {k: _as_str(v) for k, v in raw_defaults.items()}

        if os.path.exists(os.path.join(MANAGEMENT_BASE_DIR, "default_app_template")):
            print(MANAGEMENT_BASE_DIR)

        # Apply as parser defaults. Keys must match the option 'dest' names from upstream.
        # Common dest names include: template, extension, name, exclude, directory, noinput
        if normalized:
            parser.set_defaults(**normalized)
