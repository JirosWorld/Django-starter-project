{% comment %}

.. image:: https://requires.io/bitbucket/maykinmedia/default-project/requirements.svg?branch=master
     :target: https://requires.io/bitbucket/maykinmedia/default-project/requirements/?branch=master
     :alt: Requirements status

===============
Getting started
===============

Below you'll find the steps to create a Django project from scratch, using the
Maykin Media starting template. The ``<project_root>`` is typically placed in
your home directory or ``/srv/sites/``. It can be named anything but typical
examples are ``corporate``, ``website`` or more specific like
``acme-website``:

.. code-block:: bash

    $ mkdir <project_root>
    $ cd <project_root>

Create the virtual environment that holds your copy of Python and relevant
libraries:

.. code-block:: bash

    $ python -m venv env
    $ source env/bin/activate
    $ pip install "django<3.3"  # Latest LTS version (3.2.x)

Start a new Django project, named ``<project_name>``, using the template. It
can be usefull to use a ``<project_name>`` that serves as namespace in your
code, like ``maykinmedia``:

.. code-block:: bash

    $ django-admin startproject --template=https://bitbucket.org/maykinmedia/default-project/get/master.zip --extension=py,rst,html,gitignore,json,ini,js,sh,cfg,yml,example --name Dockerfile <project_name> .
    $ rm -rf ci/  # only used for jenkins CI

Create an empty Git repository

.. code-block:: bash

    $ git init


You'll need pip-compile to generate the pinned versions of the requirements:

.. code-block:: bash

    $ pip install 'pip<22' setuptools --upgrade (optionally)
    $ pip install pip-tools
    $ ./bin/compile_dependencies.sh

Modify the ``README.rst`` to be suitable for this project.

Once the project is ready, create a repository online and commit the files to
the repository:

.. code-block:: bash

    $ git remote add origin git@bitbucket.org:maykinmedia/<repo>.git
    $ git add --all
    $ git commit -m "Initial project layout."
    $ git push origin master

You'll now have a starting point for your new project. Continue to the
installation instructions (INSTALL.rst) and start at step 3.


Additions
=========

If you want to configure your Django settings module automatically:

.. code-block:: bash

    $ echo "export DJANGO_SETTINGS_MODULE='<project_name>.conf.dev'" >> env/bin/activate
    $ echo "export DJANGO_SETTINGS_MODULE=''" >> env/bin/deactivate

In case you are using `virtualenvwrapper`_ you can create the virtual
environment using:

.. code-block:: bash

    $ mkvirtualenvwrapper <project_name>
    $ echo "export DJANGO_SETTINGS_MODULE='<project_name>.conf.dev'" >> $WORKON_HOME/<project_name>/bin/postactivate
    $ workon <project_name>  # Reload virtualenv.


**NOTE:** The section above will not be included in your project's README.
Below you'll see the actual project README template.

.. _default-apps: https://bitbucket.org/maykinmedia/default-apps/src
.. _virtualenvwrapper: https://virtualenvwrapper.readthedocs.org/en/latest/


{% endcomment %}==================
{{ project_name }}
==================

:Version: 0.1.0
:Source: https://bitbucket.org/maykinmedia/{{ project_name|lower }}
:Keywords: ``<keywords>``
:PythonVersion: 3.9

|build-status| |requirements|

``<oneliner describing the project>``

Developed by `Maykin Media B.V.`_ for ``<client>``


Introduction
============

``<describe the project in a few paragraphs and briefly mention the features>``


Documentation
=============

See ``INSTALL.rst`` for installation instructions, available settings and
commands.


References
==========

* `Issues <https://taiga.maykinmedia.nl/project/{{ project_name|lower }}>`_
* `Code <https://bitbucket.org/maykinmedia/{{ project_name|lower }}>`_


.. |build-status| image:: http://jenkins.maykin.nl/buildStatus/icon?job=bitbucket/{{ project_name|lower }}/master
    :alt: Build status
    :target: http://jenkins.maykin.nl/job/{{ project_name|lower }}

.. |requirements| image:: https://requires.io/bitbucket/maykinmedia/{{ project_name|lower }}/requirements.svg?branch=master
     :target: https://requires.io/bitbucket/maykinmedia/{{ project_name|lower }}/requirements/?branch=master
     :alt: Requirements status


.. _Maykin Media B.V.: https://www.maykinmedia.nl
