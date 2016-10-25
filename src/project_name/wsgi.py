"""
WSGI config for {{ project_name }} project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os
import site
import sys

from django.core.wsgi import get_wsgi_application


def setupenv():

    cur_dir = os.getcwd()

    # Remember original sys.path.
    prev_sys_path = list(sys.path)

    # we add currently directory to path and change to it
    mydir = os.path.dirname(os.path.abspath(__file__))

    pwd = os.getenv('VIRTUAL_ENV', None)
    if pwd is None:
        pwd = os.path.join(mydir, os.path.join('..', '..', 'env'))
    os.chdir(pwd)
    sys.path = [pwd, os.path.join(mydir, '..')] + sys.path

    # find the site-packages within the local virtualenv
    for python_dir in os.listdir('lib'):
        site_packages_dir = os.path.join('lib', python_dir, 'site-packages')
        if os.path.exists(site_packages_dir):
            site.addsitedir(os.path.abspath(site_packages_dir))

    # Reorder sys.path so new directories at the front.
    new_sys_path = []
    for item in list(sys.path):
        if item not in prev_sys_path:
            new_sys_path.append(item)
            sys.path.remove(item)
    sys.path[:0] = new_sys_path

    # return back to original location, otherwise runserver throws exceptions
    os.chdir(cur_dir)


def init_newrelic():
    if os.environ.get('PROJECT_ROOT'):
        try:
            import newrelic.agent
            newrelic.agent.initialize(os.path.join(os.environ.get('PROJECT_ROOT'), 'newrelic.ini'), 'production')
        except Exception as e:
            print("Could not initialize New Relic APM, ignoring:")
            print(e)


setupenv()
init_newrelic()

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
