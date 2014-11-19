import time

from settings import *

#
# Standard Django settings.
#

DEBUG = True
TEMPLATE_DEBUG = DEBUG
WSGI_APPLICATION = '{{ project_name|lower }}.wsgi.wsgi_test.application'

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
        'TEST_NAME': 'test_{{ project_name|lower }}_{0}'.format(time.time())
    }
}

INSTALLED_APPS += [
    'django_jenkins',
]

PROJECT_APPS = [app for app in INSTALLED_APPS if app.startswith('{{ project_name|lower }}')]

JENKINS_TASKS = (
    'django_jenkins.tasks.run_pylint',
    'django_jenkins.tasks.with_coverage',
    'django_jenkins.tasks.run_pep8',
)

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

LOGGING['loggers'].update({
    'django': {
        'handlers': ['django'],
        'level': 'WARNING',
        'propagate': True,
    },
})


# Skip migrations in Django 1.7, see: https://gist.github.com/nealtodd/2869341f38f5b1eeb86d
