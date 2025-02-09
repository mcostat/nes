from .base import *

DEBUG = False
IS_TESTING = False

AXES_ENABLED = True

COMPRESS_OFFLINE = True

CSRF_USE_SESSIONS = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 60 * 60
