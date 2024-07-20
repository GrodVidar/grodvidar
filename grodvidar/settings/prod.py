import os
from pathlib import Path
from .base import BASE_DIR

import dj_database_url


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

DATABASES = {
    'default': dj_database_url.config(
        env="DATABASE_URL",
        conn_max_age=500,
        conn_health_checks=True,
        ssl_require=True,
    ),
}

MEDIA_ROOT = os.path.join(BASE_DIR, 'day_counter/media')


DOMAIN = 'https://grodvidar.com'

EMAIL_USE_TLS = True

