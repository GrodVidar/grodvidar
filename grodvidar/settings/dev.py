import os
import environ
from pathlib import Path
from .base import BASE_DIR

env = environ.Env()
environ.Env.read_env()


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

MEDIA_ROOT = os.path.join(BASE_DIR, 'day_counter/media')

SENDGRID_SANDBOX_MODE_IN_DEBUG = True

DOMAIN = '127.0.0.1:8000'

