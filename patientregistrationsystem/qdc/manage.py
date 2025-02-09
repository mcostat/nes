#!/usr/bin/env python3
import os
import sys

if __name__ == "__main__":
    SETTINGS = "qdc.settings.prod"

    if "test" in sys.argv:
        SETTINGS = "qdc.settings.test"
    elif "runserver" in sys.argv:
        SETTINGS = "qdc.settings.dev"

    os.environ["DJANGO_SETTINGS_MODULE"] = SETTINGS

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?",
        ) from exc

    execute_from_command_line(sys.argv)
