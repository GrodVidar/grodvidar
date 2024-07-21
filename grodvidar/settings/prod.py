import os
from pathlib import Path
from .base import BASE_DIR

import dj_database_url


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

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


DOMAIN = 'https://grodvidar.com'

EMAIL_USE_TLS = True

# AWS S3 SETTINGS
AWS_BUCKET_URL = os.environ.get('AWS_BUCKET_URL')

MEDIA_URL = AWS_BUCKET_URL + '/media/'

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "access_key": os.environ.get("AWS_ACCESS_KEY"),
            "secret_key": os.environ.get("AWS_SECRET_ACCESS_KEY"),
            "bucket_name": os.environ.get("AWS_STORAGE_BUCKET_NAME"),
            "location": "media",
            "region_name": "eu-central-1",
        }
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    }
}
