import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'django-insecure-q(q!iao7xf1yj^+f0w1mk=@z__shavcv9%4-v$yr)pagy1jnul'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'exchange',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'rest_framework',
    'django.contrib.staticfiles'
]

AUTH_USER_MODEL = 'exchange.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ItemExchangeApplication.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),  # If using a global templates directory
            # Or if templates are within apps, you can leave DIRS empty or include specific paths
        ],
        'APP_DIRS': True,  # This tells Django to look for templates within each app's 'templates' folder
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ItemExchangeApplication.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dbitemexchange',
        'USER': 'root',
        'PASSWORD': 'admin123',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Ensure session engine is configured
SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Default: stores session in database

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

LOGIN_URL = '/login/'