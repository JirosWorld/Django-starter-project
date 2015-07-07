Apache + mod-wsgi configuration
===============================

An example Apache2 vhost configuration follows::

    WSGIDaemonProcess {{ project_name|lower }}-<target> threads=5 maximum-requests=1000 user=<user> group=staff
    WSGIRestrictStdout Off

    <VirtualHost *:80>
        ServerName my.domain.name

        ErrorLog "/srv/sites/{{ project_name|lower }}/log/apache2/error.log"
        CustomLog "/srv/sites/{{ project_name|lower }}/log/apache2/access.log" common

        WSGIProcessGroup {{ project_name|lower }}-<target>

        Alias /media "/srv/sites/{{ project_name|lower }}/media/"
        Alias /static "/srv/sites/{{ project_name|lower }}/static/"

        WSGIScriptAlias / "/srv/sites/{{ project_name|lower }}/src/{{ project_name|lower }}/wsgi/wsgi_<target>.py"
    </VirtualHost>


Nginx + uwsgi + supervisor configuration
========================================

Supervisor/uwsgi:
-----------------

.. code::

    [program:uwsgi-{{ project_name|lower }}-<target>]
    user = <user>
    command = /srv/sites/{{ project_name|lower }}/env/bin/uwsgi --socket 127.0.0.1:8001 --wsgi-file /srv/sites/{{ project_name|lower }}/src/{{ project_name|lower }}/wsgi/wsgi_<target>.py
    home = /srv/sites/{{ project_name|lower }}/env
    master = true
    processes = 8
    harakiri = 600
    autostart = true
    autorestart = true
    stderr_logfile = /srv/sites/{{ project_name|lower }}/log/uwsgi_err.log
    stdout_logfile = /srv/sites/{{ project_name|lower }}/log/uwsgi_out.log
    stopsignal = QUIT

Nginx
-----

.. code::

    upstream django_{{ project_name|lower }}_<target> {
      ip_hash;
      server 127.0.0.1:8001;
    }

    server {
      listen :80;
      server_name  my.domain.name;

      access_log /srv/sites/{{ project_name|lower }}/log/nginx-access.log;
      error_log /srv/sites/{{ project_name|lower }}/log/nginx-error.log;

      location /500.html {
        root /srv/sites/{{ project_name|lower }}/src/{{ project_name|lower }}/templates/;
      }
      error_page 500 502 503 504 /500.html;

      location /static/ {
        alias /srv/sites/{{ project_name|lower }}/static/;
        expires 30d;
      }

      location /media/ {
        alias /srv/sites/{{ project_name|lower }}/media/;
        expires 30d;
      }

      location / {
        uwsgi_pass django_{{ project_name|lower }}_<target>;
      }
    }
