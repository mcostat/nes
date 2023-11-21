#!/bin/sh

echo "INFO: Setup NES"

echo "	INFO: makemigrations"
python3 -u manage.py makemigrations || true
echo "	INFO: Migrate"
python3 -u manage.py migrate || true

echo "	INFO create cachetable"
python3 -u manage.py createcachetable || true

echo "	INFO: colectstatic"
mkdir -p static || true
python3 -u manage.py collectstatic --no-input || true

echo "  INFO: compress"
python3 -u manage.py compress --force || true
python3 -u manage.py collectstatic --no-input || true
python manage.py runserver --nostaticpython manage.py runserver --nostatic