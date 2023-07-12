import os
import environ
from pathlib import Path

env = environ.Env()
environ.Env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

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

