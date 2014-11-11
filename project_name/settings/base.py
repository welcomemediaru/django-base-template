# coding: utf-8
"""
This is your project's main settings file that can be committed to your
repo. If you need to override a setting locally, use local.py
"""

import os
import sys
import logging

# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured


def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        return os.environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)

gettext = lambda s: s

# Your project root
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__) + "../../../")

# There should be no __init__.py in apps folder
# To import use `from appname.models import ModelName`,
# not `from apps.appname import ModelName`
sys.path.insert(0, os.path.join(PROJECT_ROOT, "apps"))

SUPPORTED_NONLOCALES = ['media', 'admin', 'static']

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru'

LANGUAGES = (
    ('ru', gettext('ru')),
)


# Defines the views served for root URLs.
ROOT_URLCONF = '{{ project_name }}.urls'

# Application definition
INSTALLED_APPS = (
    # Django cms admin styles
    'djangocms_admin_style',
    'djangocms_text_ckeditor',

    # Django contrib apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.syndication',
    'django.contrib.staticfiles',

    # Third-party apps, patches, fixes
    'debug_toolbar',
    'compressor',
    # 'django_select2',
    'easy_thumbnails',
    'image_cropping',

    # Database migrations
    'south',

    # Application base, containing global templates.
    'base',

    # django-cms and it's reqs
    'cms',
    'mptt',
    'menus',
    'sekizai',

    # django-cms plugins
    'djangocms_style',
    'djangocms_column',
    'djangocms_file',
    'djangocms_flash',
    'djangocms_googlemap',
    'djangocms_inherit',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_teaser',
    'djangocms_video',
    'reversion',

    # Local apps, referenced via appname
)

# Place bcrypt first in the list, so it will be the default password hashing
# mechanism
PASSWORD_HASHERS = (
    # 'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    # 'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
)

# Sessions
#
# By default, be at least somewhat secure with our session cookies.
SESSION_COOKIE_HTTPONLY = True

# Set this to true if you are using https
SESSION_COOKIE_SECURE = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.example.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.example.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.example.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

# URL prefix for static files.
# Example: "http://media.example.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Moscow'

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # django-cms middleware
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
]

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.i18n',
    'django.core.context_processors.static',
    'django.core.context_processors.csrf',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    # django-cms context processors
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
]

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    ('pyjade.ext.django.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)


# def custom_show_toolbar(request):
#     """ Only show the debug toolbar to users with the superuser flag. """
#     return request.user.is_superuser


DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    # 'SHOW_TOOLBAR_CALLBACK': (
    #     '{{ project_name }}.settings.base.custom_show_toolbar'),
    'HIDE_DJANGO_SQL': True,
    'TAG': 'body',
    'SHOW_TEMPLATE_CONTEXT': True,
    'ENABLE_STACKTRACES': True,
}
DEBUG_TOOLBAR_PATCH_SETTINGS = False

# DEBUG_TOOLBAR_PANELS = (
#     #'debug_toolbar_user_panel.panels.UserPanel',
#     'debug_toolbar.panels.version.VersionDebugPanel',
#     'debug_toolbar.panels.timer.TimerDebugPanel',
#     'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
#     'debug_toolbar.panels.headers.HeaderDebugPanel',
#     'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
#     'debug_toolbar.panels.template.TemplateDebugPanel',
#     'debug_toolbar.panels.sql.SQLDebugPanel',
#     'debug_toolbar.panels.signals.SignalDebugPanel',
#     'debug_toolbar.panels.logger.LoggingPanel',
# )

# Specify a custom user model to use
# AUTH_USER_MODEL = 'accounts.MyUser'

FILE_UPLOAD_PERMISSIONS = 0o0664

# The WSGI Application to use for runserver
WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

# Define your database connections
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Recipients of traceback emails and other notifications.
ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)
MANAGERS = ADMINS

# SECURITY WARNING: don't run with debug turned on in production!
# Debugging displays nice error messages, but leaks memory. Set this to False
# on all server instances and True only for development.
DEBUG = TEMPLATE_DEBUG = False

# Is this a development instance? Set this to True on development/master
# instances and False on stage/prod.
DEV = False

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["{{ project_name }}.0-wm.ru"]

# SECURITY WARNING: keep the secret key used in production secret!
# Hardcoded values can leak through source control.
# This is an example method of getting the value from an environment setting.
# Uncomment to use, and then make sure you set the SECRET_KEY environment
# variable.
# This is good to use in production, and on services that support it such as
# Heroku.
# SECRET_KEY = get_env_setting('SECRET_KEY')

INTERNAL_IPS = ('127.0.0.1')

# Django-compressor settings for less files
COMPRESS_PRECOMPILERS = (
    ('text/less', 'node_modules/less/bin/lessc {infile} {outfile}'),
)

# django-cms settings
CMS_LANGUAGES = {
    ## Customize this
    'default': {
        'hide_untranslated': False,
        'redirect_on_fallback': True,
        'public': True,
    },
    1: [
        {
            'redirect_on_fallback': True,
            'code': 'ru',
            'hide_untranslated': False,
            'name': gettext('ru'),
            'public': True,
        },
    ],
}

CMS_TEMPLATES = (
    ## Customize this
    ('base/page.jade', u'Страница'),
    ('base/index.jade', u'Главная страница')
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}


# Enable this option for memcached
# CACHE_BACKEND= "memcached://127.0.0.1:11211/"

# Set this to true if you use a proxy that sets X-Forwarded-Host
# USE_X_FORWARDED_HOST = False

SERVER_EMAIL = "webmaster@{{ project_name }}.0-wm.ru"
DEFAULT_FROM_EMAIL = "webmaster@{{ project_name }}.0-wm.ru"
SYSTEM_EMAIL_PREFIX = "[{{ project_name }}]"

## Log settings

LOG_LEVEL = logging.INFO
HAS_SYSLOG = True
SYSLOG_TAG = "http_app_{{ project_name }}"  # Make this unique to your project.
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
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

SITE_ID = 1

from easy_thumbnails.conf import Settings as thumbnail_settings

THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS
