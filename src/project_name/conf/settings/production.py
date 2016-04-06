from .base import *

#
# Standard Django settings.
#

DEBUG = False
TEMPLATE_DEBUG = DEBUG
ENVIRONMENT = 'production'
SHOW_ALERT = False

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
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Memcached cache backend setup.
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:11211',
#     }
# }

# Caching templates.
TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

# Caching sessions.
# SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

# Production logging facility.
LOGGING['loggers'].update({
    '{{ project_name|lower }}': {
        'handlers': ['project'],
        'level': 'WARNING',
        'propagate': True,
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
