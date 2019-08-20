#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRESQL_USERNAME" --dbname "$POSTGRESQL_DATABASE" <<-EOSQL
         CREATE DATABASE {{ project_name|lower }};
         GRANT ALL PRIVILEGES ON DATABASE {{ project_name|lower }} TO $POSTGRESQL_USERNAME;
EOSQL

