"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

""" here we have added parent after second parent such that it will go the base dirrectory manage.py"""
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-qm$5ftn=t2b%rf^z#rfe767q3_!%tatg2$po-y-gde!fq0boh0"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["yourdomain.com", "127.0.0.1", "localhost:8080"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",  # for session
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "store",
    "basket",
    "account",
    "django_countries",
    "payment",
    "orders",
    "mptt",
    # rest framework
    "rest_framework",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",  # for session
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                #'store.views.categories'
                "store.context_processors.categories",  # to make the categories available in all templates
                "basket.context_processors.basket",  # to make the basket available in all templates
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static/")]


MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Add or change a related_name argument to the definition for 'auth.User.user_permissions' or 'accounts.UserBase.user_permissions'
# Custom user model

# AUTH_USER_MODEL = "account.UserBase"
AUTH_USER_MODEL = "account.Customer"  # Customer table we have renamed
LOGIN_REDIRECT_URL = "/account/dashboard"
LOGIN_URL = "/account/login/"

# Email setting
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# stripe payment
PUBLISHABLE_KEY = (
    "pk_test_51JU92jSIhpZR8wXzBGMaH7rNtDzF9F3YEje9dG81GDbwvRtjbLzoh3aMO4JMhywcrkNXn3fssDLGqKtToYDHwHb300CcY5uDUH"
)
STRIPE_PAYMENT_SECRET = (
    "sk_test_51JU92jSIhpZR8wXzajV7kQOUIwJLeqTOQCCts989MB36MOGCpTCqMHuizU1gFtt1hSPbC0Hlf0eY9OK2M3krOrWR00Kpz1KPF6"
)
# stripe end point for this we need to run the cmd in the downloaded stripe cli in that we have metion this below command
# we can do cmd in visual studio code
# stripe listen --forward-to localhost:8080/payment/webhook
STRIPE_ENDPOINT_SECRET = "whsec_jkqWK0UN7zrynNa7gu3ptIkBCUpmyYKA"