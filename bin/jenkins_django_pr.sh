#!/bin/bash
virtualenv env -p python3

export DJANGO_SETTINGS_MODULE={{ project_name|lower }}.conf.test
env/bin/pip install -r requirements/test.txt

# install front-end deps
echo "Installing front end dependencies..."
npm install  # invokes jspm install

# compile sass to css
# echo "Compiling sass..."
# gulp sass
# SASS_COMPILE_FAIL=$?

echo "Running Django staticfiles..."
env/bin/python manage.py collectstatic --link --noinput
env/bin/python manage.py systemjs_bundle

echo "Starting tests"
(env/bin/python manage.py jenkins --project-apps-tests \
    --liveserver=localhost:8082-8179 \
    --verbosity 2 \
    --noinput \
    --enable-coverage \
    --pep8-rcfile=pep8.rc \
    --pylint-rcfile=pylint.rc \
    --coverage-rcfile=.coveragerc
)
TESTS_FAIL=$?

echo "Cleaning up uploaded files..."
rm -rf media/*

# exit code so that the whole build fails if any step fails
! (( $TESTS_FAIL ))
