#!/usr/bin/env python
# bootstrap.py
# Bootstrap and setup a virtualenv with the specified requirements.txt
import os
import sys
import shutil
from subprocess import call
import argparse 
from tempfile import mkstemp
from shutil import move

description = """
Set up my development environment for me!
"""

project_name = '{{ project_name|lower }}'

parser = argparse.ArgumentParser(description=description)
parser.add_argument('target', choices=['production','staging','test','development'],
                    help='production/staging/development')
parser.add_argument('--project', default=project_name,
                    help='Name of the project in your src directory, "%s" by default' % project_name)
parser.add_argument('--env', default='env',
                    help='Directory name for virtualenv, "env" by default')

args = parser.parse_args()

def replace_wsgi_settings(target):
    path = os.path.join('src', project_name, 'wsgi.py')
    file_handle, abs_path = mkstemp()
    new_file = open(abs_path, 'w')
    old_file = open(path, 'r')
    for line in old_file:
        if line.startswith("os.environ.setdefault"):
            new_file.write('os.environ.setdefault["DJANGO_SETTINGS_MODULE", "%s.settings_%s"]\n' % (project_name, target))
        else:
            new_file.write(line)
    new_file.close()
    os.close(file_handle)
    old_file.close()
    os.remove(path)
    move(abs_path, path)

def append_settings_activate(project, target, env):
    if os.name == 'posix':
        f = open('%s/bin/activate' % env, 'a')
        f.write("\nexport DJANGO_SETTINGS_MODULE='%s.conf.settings_%s'\n" %
                (project, target))
        f.close()
    if os.name == 'nt': # NOTE: Still to test in Windows
        f = open('%s\Scripts\activate.bat', 'a')
        f.write("\nset DJANGO_SETTINGS_MODULE='%s.conf.settings_%s'\n" %
                (project, target))
        f.close()

def main():
    virtualenv = args.env
    file_path = os.path.dirname(__file__)
    print("\n== Building virtualenv ==\n")
    call("virtualenv " + virtualenv, 
         shell=True)

    print("\n== Ensuring the correct settings-file is used in activate and wsgi.py ==\n")
    append_settings_activate(args.project, args.target, args.env)
    replace_wsgi_settings(args.target)

    call(os.path.join(virtualenv, "bin", "pip") + " install -r requirements/%s.txt" % args.target, shell=True)

    print("""
== Next steps ==

. %s/bin/activate
python src/manage.py syncdb --migrate
python src/manage.py collectstatic --link
python src/manage.py runserver

""" % args.env)

if __name__ == "__main__":
    main()
    sys.exit(0)
