#!/bin/sh
set -e

# Entrypoint only variable
NES_PROJECT_PATH="$NES_DIR/patientregistrationsystem/qdc"

echo "INFO: Starting Development entrypoint.sh"

if [ "$NES_DB_TYPE" != "pgsql" ]; then
    echo "Unfortunately, for the time being, NES only works with PostgreSQL."
    exit 1
fi

while ! nc -z "$NES_DB_HOST" "$NES_DB_PORT"; do
    sleep 0.2
done
echo "INFO: Database OK"

while ! nc -z "$LIMESURVEY_HOST" "$LIMESURVEY_PORT"; do
    sleep 0.2
done
echo "INFO: Limesurvey OK"

sh "$NES_PROJECT_PATH/setup_nes.sh" vscode

echo "INFO: Done initializing data"

echo "INFO: Starting Redis"
service redis-server start

echo "INFO: entrypoint.sh finished"

exec "$@"
