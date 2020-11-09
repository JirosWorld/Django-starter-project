#!/bin/bash
exec celery flower --app {{ project_name|lower }} --workdir src
