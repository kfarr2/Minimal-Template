"""
Django settings for mintemplate project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from fnmatch import fnmatch
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages import constants as messages
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP, LOGGING, AUTHENTICATION_BACKENDS
from varlet import variable
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError:
    pass

here = lambda *path: os.path.normpath(os.path.join(os.path.dirname(__file__), *path))
ROOT = lambda *path: here("../", *path)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = variable("DEBUG", True)

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

SESSION_COOKIE_DOMAIN = ".nip.io"

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mintemplate.home',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mintemplate.urls'

WSGI_APPLICATION = 'mintemplate.wsgi.application'



# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = ROOT("static")

STATICFILES_DIRS = (
            # Put strings here, like "/home/html/static" or "C:/www/django/static".
                # Always use forward slashes, even on Windows.
                    # Don't forget to use absolute paths, not relative paths.
                    here("static"),
                )

MEDIA_URL = '/media/'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ROOT("media")

TMP_ROOT = ROOT("tmp")

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    here("templates"),
    ROOT("mintemplate/static"),
)




# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%-+3mr!n@4u9#bwyc9m#c)@gkp!b@+6h+)_$sj^9hj1#tm@msj'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': variable("DB_ENGINE", 'django.db.backends.mysql'),
        'NAME': variable("DB_NAME", 'mintemplate'),
        'USER': variable("DB_USER", 'root'),
        'PASSWORD': variable("DB_PASSWORD", ''),
    }
}
