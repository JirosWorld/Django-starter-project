{% comment %}

[![Requirements Status](https://requires.io/bitbucket/maykinmedia/default-project/requirements.svg?branch=master)](https://requires.io/bitbucket/maykinmedia/default-project/requirements/?branch=master)

![Requirements Status](https://requires.io/bitbucket/maykinmedia/default-project/requirements.svg?branch=master)

Get started
===========

Below you'll find the steps to create a Django project from scratch, using the
Maykin Media starting template. The ``<project_root>`` is typically placed in
your home directory or ``/srv/sites/``. It can be named anything but typical
examples are ``corporate``, ``website`` or more specific like
``acme-website``::

    $ mkdir <project_root>
    $ cd <project_root>

Create the virtual environment that holds your copy of Python and relevant
libraries::

    $ virtualenv env or virtualenv --python=/usr/bin/python3.4 env
    $ source env/bin/activate
    $ pip install django

Start a new Django project, named ``<project_name>``, using the template. It
can be usefull to use a ``<project_name>`` that serves as namespace in your
code, like ``maykinmedia``::

    $ django-admin startproject --template=https://bitbucket.org/maykinmedia/default-project/get/master.zip --extension=py,rst,rb,html,gitignore,json,ini,js,sh,cfg,properties <project_name> .

You'll need pip-compile to generate the pinned versions of the requirements::

    $ pip install pip setuptools --upgrade (optionally)
    $ pip install pip-tools
    $ cd requirements
    $ pip-compile base.in
    $ cd ..

Once the project is ready, create a repository online and commit the files to
the repository::

    $ git init
    $ git remote add origin git@bitbucket.org:maykinmedia/<repo>.git
    $ git add --all
    $ git commit -m "Initial project layout."
    $ git push origin master

You'll now have a starting point for your new project. Continue to the
installation instructions below and start at step 3.

To start the project, you can continue to the Installation section, bullet 3.


**Default apps**

You can add boilerplate apps from here: https://bitbucket.org/maykinmedia/default-apps/src

Simply add the app (folder name) to the project by using::

    git archive --remote=git@bitbucket.org:maykinmedia/default-apps.git develop <app> | tar -x -C src/<project_name>


**Additions**

If you want to configure your Django settings module automatically::

    $ echo "export DJANGO_SETTINGS_MODULE='<project_name>.conf.dev'" >> env/bin/activate
    $ echo "export DJANGO_SETTINGS_MODULE=''" >> env/bin/deactivate

In case you are using [Virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/) you can create the virtual environment in this way::

    $ mkvirtualenvwrapper <project_name>
    $ echo "export DJANGO_SETTINGS_MODULE='<project_name>.conf.dev'" >> $WORKON_HOME/<project_name>/bin/postactivate
    $ workon <project_name>  # Reload virtualenv.


**NOTE:** The section above will not be included in your project's README.
Below you'll see the actual project README template.

{% endcomment %}
[![Requirements Status](https://requires.io/bitbucket/maykinmedia/{{ project_name|lower }}/requirements.svg?branch=master)](https://requires.io/bitbucket/maykinmedia/{{ project_name|lower }}/requirements/?branch=master)

Project layout
==============

The project layout was made in such a way that code is seperated from non-code
files that you typically want to serve in another way (static and media files)
or keep in a different location (like the virtual environment)::

    {{ project_name|lower }}
    |
    +-- bin                 -- Usefull scripts (mostly for developers).
    |
    +-- build               -- All Gulp tasks.
    |
    +-- doc                 -- Documentation source and generated files.
    |
    +-- env                 -- Virtual environment files.
    |
    +-- log                 -- All log files are stored here.
    |
    +-- media               -- Default location for uploaded media files.
    |
    +-- requirements        -- Project requirements for each type of installation.
    |
    +-- src                 -- Container for one or more source directories.
    |   |
    |   +-- {{ project_name|lower }}
    |       |
    |       +-- conf        -- Django settings files.
    |       |
    |       +-- js          -- JavaScript source files.
    |       |
    |       +-- sass        -- Sass (css pre-processor) source files.
    |       |
    |       +-- static      -- Default location for project static files.
    |       |
    |       +-- templates   -- Project templates.
    |       |
    |       +-- test        -- Automated tests.
    |       |
    |       +-- utils       -- Project-wide utility functions.
    |       |
    |       +-- ...         -- Project specific applications.
    |
    +-- static              -- Default location for collected static files.


Installation
============

New installations (for development or production) should follow the steps
below.

1. Navigate to the location where you want to place your project.

2. Get the code::

    $ git clone ssh://git@bitbucket.org/maykinmedia/{{ project_name|lower }}.git
    $ cd {{ project_name|lower }}

3. Bootstrap the virtual environment and install all required libraries. The
   ``bootstrap.py`` script basically sets the proper Django settings file to be
   used::

    $ python bootstrap.py <production|staging|test|dev>

4. Activate your virtual environment and create the statics and database::

    $ source env/bin/activate
    $ python src/manage.py collectstatic --link
    $ python src/manage.py migrate


Developers
----------

Optionally, you can load demo data and extract demo media files::

    $ python src/manage.py loaddata demo
    $ cd media
    $ tar -xzf demo.tgz

You can now run your installation and point your browser to the address given
by this command::

    $ python src/manage.py runserver

If you are making local, machine specific, changes, add them to
``src/{{ project_name|lower }}/conf/local.py``. You can base this file on
the example file included in the same directory.

Install the front-end CLI tools if you've never installed them before::

    $ npm install -g gulp
    $ npm install

Enable watch tasks::

    $ gulp

By default this will compile the sass to css on every sass file save.

For more information on SASS, see: http://sass-lang.com/.
For more information on Node.js, see: http://nodejs.org/.


Staging and production
----------------------

See https://bitbucket.org/maykinmedia/maykin-deployment/ on how to enable
Ansible deployments.


Update installation
===================

When updating an existing installation:

1. Activate the virtual environment::

    $ cd {{ project_name|lower }}
    $ source env/bin/activate

2. Update the code and libraries::

    $ git pull
    $ pip install -r requirements/<production|staging|test|dev>.txt
    $ npm install

3. Update the statics and database::

    $ python src/manage.py collectstatic --link
    $ python src/manage.py migrate