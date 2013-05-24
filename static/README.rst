This directory only contains static media. You should serve files from this
directory directly via your webserver (ie. not via the WSGI-handler).

See: https://docs.djangoproject.com/en/1.5/howto/static-files/#serving-static-files-from-a-dedicated-server

You can get all static media for this project by doing::

    $ cd {{ project_name|lower }}
    $ source env/bin/activate
    $ cd src
    $ python manage.py collectstatic --link
