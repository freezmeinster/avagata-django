# Django settings for avagata project.

import os
import sys
import settings

PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))
sys.path.insert(0,os.path.join(PROJECT_ROOT,'apps'))
sys.path.insert(0,os.path.join(PROJECT_ROOT,'libs'))

DEBUG = settings.DEBUG
TEMPLATE_DEBUG = settings.TEMPLATE_DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'avagata_new',                      # Or path to database file if using sqlite3.
        'USER': 'avagata',                      # Not used with sqlite3.
        'PASSWORD': 'pass4avagata',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = settings.TIME_ZONE

LANGUAGE_CODE = settings.LANGUAGE_CODE

SITE_ID = settings.SITE_ID

USE_I18N = settings.USE_I18N

USE_L10N = settings.USE_L10N

MEDIA_ROOT = settings.MEDIA_ROOT

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = settings.MEDIA_URL

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = settings.STATIC_ROOT

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = settings.STATIC_URL

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = settings.ADMIN_MEDIA_PREFIX

# Additional locations of static files
STATICFILES_DIRS = settings.STATICFILES_DIRS

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = settings.STATICFILES_FINDERS

# Make this unique, and don't share it with anybody.
SECRET_KEY = settings.SECRET_KEY

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = settings.TEMPLATE_LOADERS

TEMPLATE_CONTEXT_PROCESSORS = settings.TEMPLATE_CONTEXT_PROCESSORS

MIDDLEWARE_CLASSES = settings.MIDDLEWARE_CLASSES

ROOT_URLCONF = settings.ROOT_URLCONF

TEMPLATE_DIRS = settings.TEMPLATE_DIRS

INSTALLED_APPS = settings.INSTALLED_APPS
LOGGING = settings.LOGGING
