"""
A helper-script for our wsgi files that loads the virtualenv libraries
and places them in the front of our sys.path, overriding any system-level
python libraries we might have installed.
"""

import os
import site
import sys

# Remember original sys.path.
prev_sys_path = list(sys.path)

# we add currently directory to path and change to it
mydir = os.path.dirname(os.path.abspath(__file__))

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
