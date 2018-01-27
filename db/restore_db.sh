#!/bin/bash



gunzip -c /backup/timezones_project_db.gz | psql --username postgres
