import os
import site
import sys


def setupenv():

    cur_dir = os.getcwd()

    # Remember original sys.path.
    prev_sys_path = list(sys.path)

    # we add currently directory to path and change to it
    mydir = os.path.dirname(os.path.abspath(__file__))

    pwd = os.getenv('VIRTUAL_ENV', None)
    if pwd is None:
        pwd = os.path.join(mydir, os.path.join('..', '..', '..', 'env'))
    os.chdir(pwd)
    sys.path = [pwd, os.path.join(mydir, '..', '..')] + sys.path

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
    except Exception, e:
        print("Could not initialize New Relic APM, ignoring:")
        print(e)
