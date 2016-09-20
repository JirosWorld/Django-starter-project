#!/bin/bash

virtualenv env --python=python3
npm install --production
./env/bin/python bootstrap.py test
. env/bin/activate
./env/bin/python src/manage.py collectstatic --link --noinput
./env/bin/python src/manage.py jenkins --settings={{ project_name }}.conf.test --project-apps-tests  --enable-coverage --pep8-ignore=W293,W291,E501,E261 --pep8-exclude=migrations,static,media --pylint-rcfile=pylint.rc
