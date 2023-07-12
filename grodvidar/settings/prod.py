import os
import environ
from pathlib import Path
from .base import BASE_DIR


env = environ.Env()
environ.Env.read_env()


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
        'TEST': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'test.db'
        },
    },
}

MEDIA_ROOT = os.path.join(BASE_DIR, 'day_counter/media')

SENDGRID_SANDBOX_MODE_IN_DEBUG = False

