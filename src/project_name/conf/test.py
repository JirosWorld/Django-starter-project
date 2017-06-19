import os

from .base import *

#
# Standard Django settings.
#

DEBUG = False

ADMINS = ()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '{{ project_name|lower }}',
        'USER': 'jenkins',
        'PASSWORD': 'jenkins',
        'HOST': '',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',  # Set to empty string for default.
        'TEST': {
            'NAME': 'test_%s' % os.getenv('JOB_NAME', default='{{ project_name|lower }}')
        }
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/stable/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

LOGGING['loggers'].update({
    'django': {
        'handlers': ['django'],
        'level': 'WARNING',
        'propagate': True,
    },
})

#
# Custom settings
#

# Show active environment in admin.
ENVIRONMENT = 'test'

#
# Django-axes
#
AXES_BEHIND_REVERSE_PROXY = False  # Required to allow FakeRequest and the like to work correctly.

#
# Library settings
#
INSTALLED_APPS += [
    'django_jenkins',
]

PROJECT_APPS = [app.rsplit('.apps.')[0] for app in INSTALLED_APPS if app.startswith('{{ project_name|lower }}')]

JENKINS_TASKS = (
    'django_jenkins.tasks.run_pylint',
    'django_jenkins.tasks.run_pep8',
)

