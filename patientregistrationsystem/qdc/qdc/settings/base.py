"""
Django settings for qdc project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from pathlib import Path
from typing import Any

from django.utils.translation import gettext_lazy as _

BASE_DIR: Path = Path(__file__).parent.parent.parent

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY: str = os.getenv("NES_SECRET_KEY", "django-insecure")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DEBUG404 = True

# Put this line in local settings to put in maintenance mode, or uncomment, and
# restart application server
# MAINTENANCE_MODE = True

# SECURITY WARNING: don't run with "is testing" in production
IS_TESTING = True

# LOGIN_URL = "/admin/login/"
OAUTH2_PROVIDER = {"PKCE_REQUIRED": False, "ALLOWED_SCHEMES": ["http", "https"], "OIDC_ENABLED ": True}
OIDC_ENABLED = True


AXES_COOLOFF_MESSAGE = _("Your account has been locked for 30 MINUTES: too many login attempts.")
AXES_FAILURE_LIMIT = 5
AXES_RESET_ON_SUCCESS = True
AXES_COOLOFF_TIME = 0.5
AXES_CACHE = "redis"
AXES_LOCKOUT_PARAMETERS = ["ip_address", ["username", "user_agent"]]

ALLOWED_HOSTS: list[str] = ["localhost", "127.0.0.1", "0.0.0.0"]


CONN_MAX_AGE = 10 * 60
CONN_HEALTH_CHECKS = True


# Content Security Policy

CSP_IMG_SRC = ["'self'", "data:"]
CSP_STYLE_SRC = ["'self'", "'unsafe-inline'"]
CSP_SCRIPT_SRC = ["'self'", "'unsafe-inline'", "http://viacep.com.br/"]
CSP_BASE_URI = "'none'"
# CSP_INCLUDE_NONCE_IN = ["script-src"] #TODO enable this as soon as possible

# CORS
CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOWED_ORIGINS = [
    "http://localhost",
    "https://localhost",
    "http://127.0.0.1",
    "https://127.0.0.1",
    "http://localhost:8080",
    "https://localhost:8080",
    "http://127.0.0.1:8080",
    "https://127.0.0.1:8080",
    "http://localhost:8000",
    "https://localhost:8000",
    "https://" + os.getenv("NES_IP", "127.0.0.1"),
    "https://" + os.getenv("NES_HOSTNAME", "localhost"),
    "https://" + os.getenv("LIMESURVEY_HOST", "limesurvey") + ":" + os.getenv("LIMESURVEY_PORT", "8080"),
    "http://" + os.getenv("LIMESURVEY_HOST", "limesurvey") + ":" + os.getenv("LIMESURVEY_PORT", "8080"),
    "http://" + os.getenv("LIMESURVEY_URL_WEB", "localhost") + ":" + os.getenv("LIMESURVEY_PORT", "8080"),
]


# Application definition

INSTALLED_APPS: list[str] = [
    "modeltranslation",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "simple_history",
    "jsonrpclib",
    "solo",
    "fixture_magic",
    "maintenance_mode",
    "rosetta",
    "axes",
    "django_extensions",
    "compressor",
    "corsheaders",
    "oauth2_provider",
]

PROJECT_APPS: list[str] = [
    "patient",
    "custom_user",
    "experiment",
    "survey",
    "export",
    "configuration",
    "plugin",
]

INSTALLED_APPS += PROJECT_APPS

MIDDLEWARE: list[str] = [
    "csp.middleware.CSPMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.http.ConditionalGetMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "simple_history.middleware.HistoryRequestMiddleware",
    "maintenance_mode.middleware.MaintenanceModeMiddleware",
    "axes.middleware.AxesMiddleware",
    "qdc.middleware.PasswordChangeMiddleware",
]

CONTEXT_PROCESSORS = {
    "maintenance_mode.context_processors.maintenance_mode",
}

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.i18n",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
            ],
            "debug": DEBUG,
        },
    },
]

AUTHENTICATION_BACKENDS: list[str] = [
    # AxesStandaloneBackend should be the first backend in the AUTHENTICATION_BACKENDS list.
    "axes.backends.AxesStandaloneBackend",
    # Django ModelBackend is the default authentication backend.
    "django.contrib.auth.backends.ModelBackend",
]

SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
SESSION_SAVE_EVERY_REQUEST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 60 * 60
SESSION_CACHE_ALIAS = "redis"

CACHE_MIDDLEWARE_ALIAS = "redis"
CACHE_MIDDLEWARE_KEY_PREFIX = ""
CACHE_MIDDLEWARE_SECONDS = 10 * 60

CACHES: dict[str, Any] = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "limesurveycache",
        "TIMEOUT": 24 * 60 * 60,
    },
    "redis": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
    },
}

COMPRESS_CACHE_BACKEND = "redis"
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = False
COMPRESS_STORAGE = "compressor.storage.GzipCompressorFileStorage"

COMPRESS_FILTERS = {
    "css": [
        "compressor.filters.css_default.CssAbsoluteFilter",
        "compressor.filters.cssmin.rCSSMinFilter",
    ],
    "js": ["compressor.filters.jsmin.JSMinFilter"],
}

ROOT_URLCONF = "qdc.urls"

WSGI_APPLICATION = "qdc.wsgi.application"

# AUTH_USER_MODEL = "custom_user.UserProfile"
# AUTH_PROFILE_MODULE = 'quiz.UserProfile'

LANGUAGE_CODE = "pt-br"

LANGUAGES = (
    (
        "pt-br",
        _("Português"),
    ),
    (
        "en",
        _("English"),
    ),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, "locale"),
    os.path.join(BASE_DIR, "qdc/locale"),
    os.path.join(BASE_DIR, "patient/locale"),
    os.path.join(BASE_DIR, "experiment/locale"),
    os.path.join(BASE_DIR, "survey/locale"),
    os.path.join(BASE_DIR, "custom_user/locale"),
    os.path.join(BASE_DIR, "export/locale"),
    os.path.join(BASE_DIR, "processing/locale"),
    os.path.join(BASE_DIR, "static_data/locale"),
)

USE_TZ = True
TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_L10N = True

# Database Translation
MODELTRANSLATION_LANGUAGES = (
    "pt-br",
    "en",
)
MODELTRANSLATION_FALLBACK_LANGUAGES = (
    "pt-br",
    "en",
)

MODELTRANSLATION_TRANSLATION_FILES = (
    "patient.translation",
    "experiment.translation",
    # '<APP2_MODULE>.translation',
)

MODELTRANSLATION_CUSTOM_FIELDS = (
    "name",
    "description",
    "abbreviated_description",
)

MODELTRANSLATION_AUTO_POPULATE = "all"

MODELTRANSLATION_PREPOPULATE_LANGUAGE = "en"

FIXTURE_DIRS = (
    "patient.fixtures",
    "experiment.fixtures",
)

# The maximum number of parameters that may be received via GET or POST
DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
    },
}

STATICFILES_DIRS: list[str] = [
    os.path.join(BASE_DIR, "static_data"),
]

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    # other finders..
    "compressor.finders.CompressorFinder",
)

STATIC_ROOT: str = os.path.join(BASE_DIR, "static")
STATIC_URL = "static/"

ADMIN_MEDIA_PREFIX = STATIC_URL + "admin/"

MEDIA_ROOT: str = os.path.join(BASE_DIR, "media")
MEDIA_URL = "media/"


ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "0.0.0.0",
    os.getenv("NES_IP", "127.0.0.1"),
    os.getenv("NES_HOSTNAME", "localhost"),
]
CSRF_TRUSTED_ORIGINS = [
    "https://localhost",
    "https://" + os.getenv("NES_IP", "127.0.0.1"),
    "https://" + os.getenv("NES_HOSTNAME", "localhost"),
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("NES_DB", "nes_db"),
        "USER": os.getenv("NES_DB_USER", "nes_user"),
        "PASSWORD": os.getenv("NES_DB_PASSWORD", "nes_password"),
        "HOST": os.getenv("NES_DB_HOST", "nes_db"),
        "PORT": os.getenv("NES_DB_PORT", "5432"),
    }
}

# LimeSurvey configuration
LIMESURVEY = {
    "URL_API": "http://" + os.getenv("LIMESURVEY_HOST", "localhost") + ":" + os.getenv("LIMESURVEY_PORT", "8080"),
    "URL_WEB": "http://" + os.getenv("LIMESURVEY_URL_WEB", "localhost") + ":" + os.getenv("LIMESURVEY_PORT", "8080"),
    "USER": os.getenv("LIMESURVEY_ADMIN_USER", "lime_admin"),
    "PASSWORD": os.getenv("LIMESURVEY_ADMIN_PASSWORD", "lime_admin_password"),
}

# Portal API configuration
PORTAL_API: dict[str, str] = {"URL": "", "PORT": "", "USER": "", "PASSWORD": ""}

# Show button to send experiments to Portal
SHOW_SEND_TO_PORTAL_BUTTON = False

# Settings to send emails
EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "")
DEFAULT_FROM_EMAIL = os.getenv("EMAIL_HOST_USER", "")
SERVER_EMAIL = EMAIL_HOST_USER

PROJECT_REPO = "https://github.com/mcostat/nes.git"

VERSION = "2.0.0"
