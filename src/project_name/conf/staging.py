from .base import *

#
# Standard Django settings.
#

DEBUG = False
WSGI_APPLICATION = '{{ project_name|lower }}.wsgi.staging.application'
ENVIRONMENT = 'staging'

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '{{ project_name|lower }}',
        'USER': '{{ project_name|lower }}',
        'PASSWORD': '{{ project_name|lower }}',
        'HOST': '',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',  # Set to empty string for default.
    }
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = '{{ secret_key }}'

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/stable/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', RAW_TEMPLATE_LOADERS),
]

LOGGING['loggers'].update({
    '': {
        'handlers': ['sentry'],
        'level': 'WARNING',
        'propagate': False,
    },
    'django': {
        'handlers': ['django'],
        'level': 'WARNING',
        'propagate': True,
    },
})

#
# django-maintenancemode
#
MAINTENANCE_MODE = False

#
# Raven
#
INSTALLED_APPS = INSTALLED_APPS + [
    'raven.contrib.django.raven_compat',
]
RAVEN_CONFIG = {
    'dsn': 'http://',
}
LOGGING['handlers'].update({
    'sentry': {
        'level': 'WARNING',
        'class': 'raven.handlers.logging.SentryHandler',
        'dsn': RAVEN_CONFIG['dsn']
    },
})
