import os

from .base import *

DEBUG = True

SECRET_KEY = "django-insecure-szn4&1bh&m9pwwkip&^!r0j4*80c)3v+k*ch6aka%-f+ye8p4%"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# smtp4dev
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.environ.get('EMAIL_HOST', "127.0.0.1")
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_PORT = os.environ.get("EMAIL_PORT", 2525)
DEFAULT_FROM_EMAIL = f"accounts@{PROJECT_NAME.lower()}.com"

# rabbitmq
RABBITMQ_USER = "guest"
RABBITMQ_PASSWORD = "guest"
RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST', 'localhost')
RABBITMQ_PORT = 5672

# celery
CELERY_BROKER_URL = "amqp://{user}:{password}@{host}:{port}/".format(
    user=RABBITMQ_USER,
    password=RABBITMQ_PASSWORD,
    host=RABBITMQ_HOST,
    port=RABBITMQ_PORT,
)

# redis
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{os.environ.get("REDIS_HOST", '127.0.0.1')}:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}
