"""
Django settings for passify project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from datetime import timedelta
from pathlib import Path

from celery.schedules import crontab

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "djoser",
    "django_user_agents",
    "customauth",
    "entries",
    "custom_commands",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_user_agents.middleware.UserAgentMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "config" / "templates",
            BASE_DIR / "customauth" / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "config.context_processors.project_name",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {
            "min_length": 10,
        },
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
    # Custom password validators
    {
        "NAME": "customauth.validators.UppercaseValidator",
    },
    {
        "NAME": "customauth.validators.LowercaseValidator",
    },
    {
        "NAME": "customauth.validators.NumberValidator",
    },
    {
        "NAME": "customauth.validators.SymbolValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Custom settings

PROJECT_NAME = "Passify"

AUTH_USER_MODEL = "customauth.CustomUser"

REST_FRAMEWORK = {
    "COERCE_DECIMAL_TO_STRING": False,
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {
        "anon": "1440/day",  # 1 rpm
        "user": "2880/day",  # 2 rpm
    },
}

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("JWT",),
    "ACCESS_TOKEN_LIFETIME": timedelta(
        days=1,
        # minutes=1,
        # seconds=10
    ),
    "UPDATE_LAST_LOGIN": True,
}

DJOSER = {
    # https://djoser.readthedocs.io/en/2.2.2/settings.html#settings
    "USER_ID_FIELD": "id",
    "USERNAME_CHANGED_EMAIL_CONFIRMATION": True,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    "SEND_CONFIRMATION_EMAIL": True,
    "SEND_ACTIVATION_EMAIL": True,
    "SEND_NEW_SIGN_IN_EMAIL": True,
    "SEND_REMINDER_EMAIL": True,
    "ACTIVATION_URL": "account/activate/{uid}/{token}",
    "USERNAME_RESET_CONFIRM_URL": "account/reset-email/{uid}/{token}",
    "PASSWORD_RESET_CONFIRM_URL": "account/reset-password/{uid}/{token}",
    "SET_USERNAME_RETYPE": True,
    "SET_PASSWORD_RETYPE": True,
    "PASSWORD_RESET_CONFIRM_RETYPE": True,
    "USERNAME_RESET_CONFIRM_RETYPE": True,
    "USER_CREATE_PASSWORD_RETYPE": True,
    "SERIALIZERS": {
        # https://djoser.readthedocs.io/en/2.2.2/settings.html#serializers
        "user_create": "customauth.serializers.UserCreateSerializer",
        "current_user": "customauth.serializers.UserSerializer",
        "user": "customauth.serializers.UserSerializer",
        "user_update": "customauth.serializers.UserSerializer",
    },
    "PERMISSIONS": {
        # https://djoser.readthedocs.io/en/2.2.2/settings.html#permissions
        "user": ["customauth.permissions.CurrentUser"],
        "user_list": ["customauth.permissions.DenyAny"],
        "user_delete": ["customauth.permissions.CurrentUser"],
        "set_username": ["customauth.permissions.CurrentUser"],
        "set_password": ["customauth.permissions.CurrentUser"],
    },
    "EMAIL": {
        # https://djoser.readthedocs.io/en/2.2.2/settings.html#email
        "activation": "customauth.email.ActivationEmail",
        "confirmation": "customauth.email.ConfirmationEmail",
        "password_reset": "customauth.email.PasswordResetEmail",
        "username_reset": "customauth.email.UsernameResetEmail",
        "password_changed_confirmation": "customauth.email.PasswordChangedConfirmationEmail",
        "username_changed_confirmation": "customauth.email.UsernameChangedConfirmationEmail",
        "new_sign_in": "customauth.email.NewSignInEmail",
        "reminder": "customauth.email.ReminderEmail",
    },
}

CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_ACCEPT_CONTENT = ["application/json"]

CELERY_BEAT_SCHEDULE = {
    "notify_users": {
        "task": "customauth.tasks.notify_users_task",
        "schedule": crontab(
            month_of_year="*/3",
            day_of_month=1,
            hour=8,
            minute=0,
        ),
    }
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": "general.log",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "": {
            "handlers": [
                "console",
                "file",
            ],
            "level": os.environ.get("DJANGO_LOG_LEVEL", "INFO"),
        }
    },
    "formatters": {
        "verbose": {
            "format": "{asctime} ({levelname}) - {name} - {message}",
            "style": "{",
        }
    },
}
