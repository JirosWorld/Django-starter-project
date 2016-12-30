import os

from .base import *

#
# Standard Django settings.
#

DEBUG = False
WSGI_APPLICATION = '{{ project_name|lower }}.wsgi.test.application'
ENVIRONMENT = 'test'

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

INSTALLED_APPS += [
    'django_jenkins',
]

PROJECT_APPS = [app for app in INSTALLED_APPS if app.startswith('{{ project_name|lower }}')]

JENKINS_TASKS = (
    'django_jenkins.tasks.run_pylint',
    'django_jenkins.tasks.run_pep8',
)

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


# Skip migrations in Django 1.7, see: https://gist.github.com/nealtodd/2869341f38f5b1eeb86d
# Migration skipping is however not recommended, if possible, use the --keepdb option,
# this is viable for develop/master builds, but not for pr's.
