#!/bin/sh
set -e

# Entrypoint only variable
NES_PROJECT_PATH="$NES_DIR/patientregistrationsystem/qdc"

echo "INFO: Setup Apache"

if [ -f /etc/apache2/sites-available/nes.conf ]; then
    echo "INFO: Apache data has already been initialized"
else
    echo "INFO: Initializing Apache data"
    sudo mkdir -p /etc/apache2/ssl-certs
    cat <<-EOF >/etc/apache2/sites-available/nes.conf
<VirtualHost *:$NES_PORT>
    ServerName $NES_IP
    ServerAlias $NES_HOSTNAME
    ServerAdmin lapis@peb.ufrj.br

    DocumentRoot $NES_PROJECT_PATH

    <Directory />
        Options FollowSymLinks
        AllowOverride None
    </Directory>

    Alias /media/ $NES_PROJECT_PATH/media/
    Alias /static/ $NES_PROJECT_PATH/static/

    <Directory $NES_PROJECT_PATH/media>
        Require all granted
    </Directory>

    <Directory $NES_PROJECT_PATH/static>
        Require all granted

        <IfModule mod_headers.c>
            <FilesMatch "\.(ico|pdf|flv|jpg|jpeg|png|gif|js|css|swf|svg)$">
                Header set Cache-Control "max-age=31536000, public"
            </FilesMatch>
        </IfModule>
    </Directory>

    <Directory $NES_PROJECT_PATH>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>

    WSGIScriptAlias / $NES_PROJECT_PATH/qdc/wsgi.py application-group=%{GLOBAL}
    WSGIDaemonProcess nes lang='en_US.UTF-8' locale='en_US.UTF-8'
    WSGIProcessGroup nes

    ErrorLog ${APACHE_LOG_DIR}/nes_error.log
    LogLevel warn
    CustomLog ${APACHE_LOG_DIR}/nes_access.log combined
</VirtualHost>
	EOF

    cat <<-EOF >/etc/apache2/sites-available/nes-ssl.conf
<IfModule mod_ssl.c>
<VirtualHost *:443>
    Protocols h2 h2c http/1.1

    ServerName $NES_IP
    ServerAlias $NES_HOSTNAME
    ServerAdmin lapis@peb.ufrj.br

    DocumentRoot $NES_PROJECT_PATH

    <Directory />
        Options FollowSymLinks
        AllowOverride None
    </Directory>

    Alias /media/ $NES_PROJECT_PATH/media/
    Alias /static/ $NES_PROJECT_PATH/static/

    <Directory $NES_PROJECT_PATH/media>
        Require all granted
    </Directory>

    <Directory $NES_PROJECT_PATH/static>
        Require all granted

        <IfModule mod_headers.c>
            <FilesMatch "\.(ico|pdf|flv|jpg|jpeg|png|gif|js|css|swf|svg|ttf|woff2)$">
                Header set Cache-Control "max-age=31536000, public"
            </FilesMatch>
        </IfModule>
    </Directory>

    <Directory $NES_PROJECT_PATH>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>

    #Alias /img/ $NES_PROJECT_PATH/img/

    WSGIScriptAlias / $NES_PROJECT_PATH/qdc/wsgi.py application-group=%{GLOBAL}
    WSGIDaemonProcess nes-ssl lang='en_US.UTF-8' locale='en_US.UTF-8'
    WSGIProcessGroup nes-ssl

    SSLEngine on

    SSLCertificateFile  /etc/apache2/ssl-certs/cert.pem
    SSLCertificateKeyFile /etc/apache2/ssl-certs/key.pem

    <FilesMatch "\.(cgi|shtml|phtml|php)$">
            SSLOptions +StdEnvVars
    </FilesMatch>
    <Directory /usr/lib/cgi-bin>
            SSLOptions +StdEnvVars
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/nes_ssl_error.log
    LogLevel warn
    CustomLog ${APACHE_LOG_DIR}/nes_ssl_access.log combined
</VirtualHost>
</IfModule>
	EOF

    sudo mkcert -key-file /etc/apache2/ssl-certs/key.pem -cert-file /etc/apache2/ssl-certs/cert.pem "$NES_HOSTNAME" "$NES_IP" localhost 0.0.0.0

    a2enmod ssl
    a2enmod http2
    a2enmod headers
    a2dissite 000-default.conf
    a2ensite nes
    a2ensite nes-ssl
fi
