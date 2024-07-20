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
            'NAME': 'GrodVidar$testdb',
        },
    },
}

MEDIA_ROOT = os.path.join(BASE_DIR, 'day_counter/media')


DOMAIN = 'https://counter.grodvidar.com'

EMAIL_USE_TLS = True

