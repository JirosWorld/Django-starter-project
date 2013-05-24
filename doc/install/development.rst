.. _install_development:

=======================
Development environment
=======================

Quick start
===========

.. note:: If you have some global utilities (like buildout, ipython, etc.) 
   installed, you could pass the option ``--system-site-packages`` to the
   ``virtualenv`` command.

#. Navigate to your local project root directory.
   
#. Setup the virtual environment and install all required libraries::

    $ cd {{ project_name|lower }}
    $ virtualenv env
    $ source env/bin/activate
    $ pip install -r requirements/development.txt
    
#. Create the statics and database::

    $ cd src
    $ export DJANGO_SETTINGS_MODULE={{ project_name|lower }}.conf.settings_development
    $ python manage.py collectstatic --link
    $ python manage.py syncdb --migrate

#. Start a local webserver::

    $ python manage.py runserver

#. In a seperate console, use Compass to compile the SASS files::

    $ cd {{ project_name|lower }}
    $ compass watch
    
#. In your webbrowser, navigate to::

    http://localhost:8000/
