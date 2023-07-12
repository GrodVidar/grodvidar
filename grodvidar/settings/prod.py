import os
import environ
from pathlib import Path

env = environ.Env()
environ.Env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['counter.grodvidar.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'GrodVidar$counter',
        'USER': 'GrodVidar',
        'PASSWORD': env('MY_SQL_PASS'),
        'HOST': 'GrodVidar.mysql.pythonanywhere-services.com',
    }
}

MEDIA_ROOT = os.path.join(BASE_DIR, 'day_counter/media')

SENDGRID_SANDBOX_MODE_IN_DEBUG = False

