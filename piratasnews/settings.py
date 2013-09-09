#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

DEBUG = os.environ.get('DEBUG')
print os.environ.get('DEBUG')
TEMPLATE_DEBUG = DEBUG

PROJECT_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_PATH, 'piratasnews.db'),
    }
}

SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = False

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '*oq23__$h5#@jgn$@xjr2jfxs&$-60@_k_lsjp22=w$6u3=6^3'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    'opps.channels.context_processors.channel_context',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    # Used in Multi-Site
    'opps.contrib.multisite.middleware.DynamicSiteMiddleware',
    # Used in Mobile Detection
    'opps.contrib.mobile.middleware.MobileDetectionMiddleware',
)

TEMPLATE_DIRS = (os.path.join(PROJECT_PATH, 'templates'),)
TEMPLATE_DIRS_WEB = TEMPLATE_DIRS
TEMPLATE_DIRS_MOBILE = (os.path.join(PROJECT_PATH, 'templates', 'mobile'),)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.redirects',
    'django.contrib.formtools',

    'opps.contrib.admin',
    'grappelli.dashboard',
    'grappelli',
    'django.contrib.admin',

    'opps.archives',
    'opps.articles',
    'opps.boxes',
    'opps.core',
    'opps.core.tags',
    'opps.containers',
    'opps.channels',
    'opps.flatpages',
    'opps.images',
    'opps.sources',
    'opps.sitemaps',
    'opps.feedcrawler',

    'south',
    'rest_framework',
)


OPPS_CHECK_MOBILE = True

#MEDIA_URL = '/media/'
MEDIA_URL = 'http://noticias.codesafe.com.br/media/'

THUMBOR_ENABLED = True
THUMBOR_MEDIA_URL = 'http://186.226.87.2:2080/media/'

TEST_RUNNER = 'django_coverage.coverage_runner.CoverageRunner'

CACHES = {'default': {
    'BACKEND': 'django.core.cache.backends.dummy.DummyCache'}}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

STATIC_URL = '/static/'
#STATIC_URL = 'http://noticias.codesafe.com.br/static/'

STATIC_ROOT = os.path.join(PROJECT_PATH, 'public', 'static')
STATICFILES_DIRS = (os.path.join(PROJECT_PATH, 'public', '_static'),)

URL_TINYMCE = STATIC_URL + "tinymce"
PATH_TINYMCE = STATIC_URL + "tinymce"

ROOT_URLCONF = 'piratasnews.urls'

##################
# LOCAL SETTINGS #
##################

# Allow any settings to be defined in local_settings.py which should be
# ignored in your version control system allowing for settings to be
# defined per machine.
try:
    from local_settings import *
except ImportError:
    pass
