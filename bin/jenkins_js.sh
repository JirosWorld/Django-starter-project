#/bin/bash

virtualenv env -p python3

export DJANGO_SETTINGS_MODULE={{ project_name|lower }}.conf.test
env/bin/pip install -r requirements/test.txt

echo "Installing front-end build tooling + dependencies"
npm install  # invokes jspm install

echo "Running collectstatic..."
env/bin/python manage.py collectstatic --link --noinput

echo "Starting tests"
xvfb-run --server-args='-screen 0, 1920x1200x16' npm test

exit_code=$?
echo "XFVB exit code: $exit_code"
exit $exit_code