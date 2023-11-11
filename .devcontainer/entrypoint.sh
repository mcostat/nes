#!/bin/sh
set -e

# Entrypoint only variable
NES_PROJECT_PATH="$NES_DIR/patientregistrationsystem/qdc"

echo "INFO: Starting entrypoint.sh"

if [ $NES_DB_TYPE != "pgsql" ]; then
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


# INITIALIZE DATA ####################################################

if [ -f $NES_DIR/.nes_initialization.placeholder ]; then
    echo "INFO: NES data has already been initialized"
else
    echo "INFO: Initializing NES data (migrations, initial, superuser, ICD, ...)"
    cd $NES_DIR/patientregistrationsystem/qdc/
    
	cat <<-EOF >/tmp/create_superuser.py
from django.contrib.auth import get_user_model
User = get_user_model()
try:
    User.objects.create_superuser("$NES_ADMIN_USER", "$NES_ADMIN_EMAIL", "$NES_ADMIN_PASSWORD")
except:
    print("Error creating super user.")
	EOF
    
    echo "	INFO: makemigrations"
    python3 -u manage.py makemigrations || true
    echo "	INFO: Migrate"
    python3 -u manage.py migrate || true
    echo "	INFO: add_initial_data.py"
    python3 -u manage.py shell < add_initial_data.py || true
    echo "	INFO: load_initial_data.py"
    python3 -u manage.py loaddata load_initial_data.json || true
    python3 -u manage.py loaddata load_eeg_initial_data.json || true
    echo "	INFO: create cachetable"
    python3 -u manage.py createcachetable || true
    echo "	INFO: create_super_user.py"
    python3 -u manage.py shell < /tmp/create_superuser.py || true
    echo "	INFO: import cid10"
    python3 -u manage.py import_icd_cid --file icd10cid10v2017.csv || true
    echo "	INFO: populate_history"
    python3 -u manage.py populate_history --auto || true

    mkdir -p static || true
    echo "	INFO: colectstatic"
    python3 -u manage.py collectstatic --no-input || true

    echo "  INFO: compress"
    python3 -u manage.py compress --force || true
    

    mkdir -p $NES_PROJECT_PATH/media/eeg_electrode_system_files/1/
    mkdir -p $NES_PROJECT_PATH/media/eeg_electrode_system_files/2/
    mkdir -p $NES_PROJECT_PATH/media/eeg_electrode_system_files/3/

    cp -r $NES_PROJECT_PATH/site_static/imgs/International_10-10_system_for_EEG.png $NES_PROJECT_PATH/media/eeg_electrode_system_files/2/International_10-10_system_for_EEG.png
    cp -r $NES_PROJECT_PATH/site_static/imgs/International_10-20_system_for_EEG.jpg $NES_PROJECT_PATH/media/eeg_electrode_system_files/3/International_10-20_system_for_EEG.jpg
    cp -r $NES_PROJECT_PATH/site_static/imgs/128_channel_HCGSN_v.1.0.png $NES_PROJECT_PATH/media/eeg_electrode_system_files/1/128_channel_HCGSN_v.1.0.png

    rm /tmp/create_superuser.py
    
    # If NES was installed from a release it won"t have a .git directory
    chown -R vscode $NES_DIR/.git || true
    chown -R vscode $NES_DIR/patientregistrationsystem
    
    touch $NES_DIR/.nes_initialization.placeholder
    chown -R nobody $NES_DIR/.nes_initialization.placeholder
fi

echo "INFO: Done initializing data"

echo "INFO: Starting Redis"
service redis-server start

echo "INFO: entrypoint.sh finished"

exec "$@"
