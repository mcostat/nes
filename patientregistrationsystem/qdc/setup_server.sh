#!/bin/sh

echo "	INFO: colectstatic"
mkdir -p static || true
python3 -u manage.py collectstatic --no-input || true

echo "  INFO: compress"
python3 -u manage.py compress --force || true
