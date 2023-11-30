#!/bin/sh
set -e

echo "INFO: Starting Production entrypoint.sh"

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

sh "$NES_DIR/scripts/setup_nes.sh" www-data
sh "$NES_DIR/scripts/setup_apache.sh"

echo "INFO: Done initializing data"

echo "INFO: Starting Redis"
service redis-server start

echo "INFO: Starting Apache"
service apache2 start

echo "INFO: entrypoint.sh finished"

exec "$@"
