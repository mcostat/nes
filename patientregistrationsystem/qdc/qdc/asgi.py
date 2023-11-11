import os
import sys

paths = [
    os.getenv("NES_DIR", "/usr/local/nes"),
    "/usr/local",
    "/usr/bin",
    "/bin",
]

for path in paths:
    if path not in sys.path:
        sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "qdc.settings.prod")

from django.core.asgi import get_asgi_application

application = get_asgi_application()
