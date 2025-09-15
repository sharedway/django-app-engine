"""
Django APP Engine
"""

from pathlib import Path
import os

__all__ = ["admin", "models", "auth", "views", "utils"]
_app_version = "0.0.1"

# Read version from file
# bump_app_version_on_new_commit.py create and update every commit

APP_BASE_DIR = Path(__file__).resolve().parent
with open(f"{APP_BASE_DIR}/app_version.txt") as app_version_file:
    _app_version = app_version_file.read()

VERSION = _app_version
default_app_config = "django_app_engine.apps.DjangoAppEngineConfig"
