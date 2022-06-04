"""
    Django settings for project project.
"""
from django.contrib import messages
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k@ljl8t%c+#=podqqy$u(adb6c+i$4b1z9)93pih023e8j1(dx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1',
                 '192.168.1.54', '192.168.1.59', '192.168.1.137']


# Application definition
INSTALLED_APPS = [
    # Красивые штучки для admin
    'django_static_fontawesome',
    'django_static_jquery3',
    'django_admin_global_sidebar',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps
    'main',
    'cart',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['main/templates', os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'admincolors.context_processors.admin_theme',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Admin customization
DJANGO_ADMIN_GLOBAL_SIDEBAR_MENUS = 'main.menus.get_simple_menus'

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

# Internationalization
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Etc/GMT+3'
USE_I18N = False
USE_L10N = False
USE_TZ = True
THOUSAND_SEPARATOR = ' '
USE_THOUSAND_SEPARATOR = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"), ]

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# Bootstrap toasts
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info-cus',
    messages.INFO: 'alert-info-cus',
    messages.SUCCESS: 'alert-success-cus',
    messages.WARNING: 'alert-warning-cus',
    messages.ERROR: 'alert-danger-cus',
}

CART_SESSION_ID = 'cart'
SESSION_COOKIE_HTTPONLY = True
SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
