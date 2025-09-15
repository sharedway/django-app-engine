"""
Just a helper to auto bump version every commit.

This ensures that @prod recompile at pip install.

"""

from packaging.version import Version, parse


app_version = "0.0.1"

with open("django_app_engine/app_version.txt") as version_file:
    app_version = version_file.read()

v = parse(app_version)

micro = v.micro
minor = v.minor
major = v.major


if micro < 1000:
    micro = micro + 1

if micro >= 999:
    micro = 0
    minor = minor + 1

if minor >= 999:
    minor = 0
    major = major + 1


with open("django_app_engine/app_version.txt", "w") as version_file:
    version_file.write(f"{major}.{minor}.{micro}")
