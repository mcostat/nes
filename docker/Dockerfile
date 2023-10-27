FROM python:3.11-slim-bookworm as wheeler

ENV PYTHONUNBUFFERED 1
ENV PYTHONOPTIMIZE 1

ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  


ARG NES_BRANCH=dev
ARG NES_DIR=/usr/local/nes
ENV NES_DIR=$NES_DIR

RUN mkdir -p "$NES_DIR"  && \
		if [ "$NES_TAG" != "unset" ]; then \
			echo Cloning tag "$NES_TAG" ;\
			wget https://github.com/neuromat/nes/archive/TAG-"${NES_TAG}".tar.gz -qO - | \
				tar xzv --strip-components=1 -C "$NES_DIR" ;\
			sed -i 's/\(psycopg2==\)[0-9.]\+/\12.7.5/' /nes/patientregistrationsystem/qdc/requirements.txt ;\
			sed -i '1isetuptools>=40.6.3' /nes/patientregistrationsystem/qdc/requirements.txt ;\
			sed -i '1ipip>=18.1' /nes/patientregistrationsystem/qdc/requirements.txt ;\
			echo 'mne>=0.17.0' >> /nes/patientregistrationsystem/qdc/requirements.txt ;\
			echo '-e "git+https://github.com/AllenInstitute/nwb-api.git#egg=nwb&subdirectory=ainwb"' >> /nes/patientregistrationsystem/qdc/requirements.txt ;\
		elif [ "$NES_BRANCH" != "unset" ]; then \
			echo Cloning "$NES_BRANCH" branch ;\
			git clone -j $(nproc) -b "$NES_BRANCH"  https://github.com/neuromat/nes.git "$NES_DIR" ;\
		else \
			echo Cloning master branch ;\
			git clone -j $(nproc) https://github.com/neuromat/nes.git "$NES_DIR" ;\
		fi


RUN mkdir -p /wheels/requirement && \
    cp $NES_DIR/patientregistrationsystem/qdc/requirements.txt /wheels/requirement

WORKDIR /wheels

RUN pip3 install -U pip setuptools wheel && \
    pip3 install -r requirement/requirements.txt && \
    pip3 wheel -r requirement/requirements.txt

FROM alpine:3.12

SHELL ["/bin/sh","-exc"]

RUN apk update && \
	apk add --no-cache \
		# Postgresql 9, due to LS incompatbilities \\
		postgresql-bdr \
		postgresql-bdr-client \
		# limesurvey - apache2  \\
		apache2 \
		# limesurvey - php  \\
		php7 \
		php7-apache2 \
		php7-ctype \
		php7-gd \
		php7-imap \
		php7-json \
		php7-ldap \
		php7-mbstring \
		php7-pdo_pgsql \
		php7-session \
		php7-simplexml \
		php7-xml \
		php7-zip \
		# git to clone and update nes  \\
		git \
		# python to run django \\
		python3 \
		py3-pip \
		# supervisord  \\
		supervisor \
		# nes dependencies \\
		graphviz \
		openblas-dev \
		hdf5-dev && \
	rm -rf /var/cache/apk/*

# SETUP POSTGRESQL ##################################################
ARG PGDATA=/var/lib/postgresql/data
ENV PGDATA=$PGDATA

RUN	mkdir -p /var/run/postgresql  && \
		chown -R postgres:postgres /var/run/postgresql  && \
		chmod 2777 /var/run/postgresql  && \
		mkdir -p "$PGDATA"  && \
		chown -R postgres:postgres "$PGDATA"  && \
		chmod 700 "$PGDATA"

VOLUME $PGDATA

# LIMESURVEY INSTALLATION ####################################################
ARG LIMESURVEY_URL_DOWNLOAD=https://github.com/LimeSurvey/LimeSurvey/archive/2.73.1+171220.tar.gz
ARG LIMESURVEY_DIR=/var/www/limesurvey
ENV LIMESURVEY_DIR=$LIMESURVEY_DIR

RUN mkdir -p "$LIMESURVEY_DIR" && \
		wget "$LIMESURVEY_URL_DOWNLOAD" -qO - | \
			tar xz --strip-components=1 -C "$LIMESURVEY_DIR" && \
		chown -R apache:apache "$LIMESURVEY_DIR" && \
		chmod -R o-rwx "$LIMESURVEY_DIR" && \
		chmod -R 770 "${LIMESURVEY_DIR}"/application/config/ && \
		chmod -R 770 "${LIMESURVEY_DIR}"/upload/ && \
		chmod -R 770 "${LIMESURVEY_DIR}"/tmp/ && \
		mkdir -p /run/apache2

VOLUME $LIMESURVEY_DIR

# NES INSTALLATION ###########################################################
ARG NES_DIR=/nes
ENV NES_DIR=$NES_DIR


RUN apt-get -y update --no-install-recommends && export DEBIAN_FRONTEND=noninteractive && \
    apt-get -y install --no-install-recommends \
    curl \
    python3-pip \
    python3-psycopg \
    libnss3-tools \
    git \
    apache2 \
    locales \
    openssl \
    libapache2-mod-wsgi-py3 \
    netcat-traditional \
    # server dependencies
    #libopenblas-dev \
    #libhdf5-dev \
    lsb-release \
    gpg \
    redis-server \
    graphviz && \
    #snapd && \
    # Remove imagemagick due to https://security-tracker.debian.org/tracker/CVE-2019-10131
    apt-get purge -y imagemagick imagemagick-6-common && \
    apt-get autoremove -y && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists* && \
    ln -s /usr/include/locale.h /usr/include/xlocale.h


# RUN curl -fsSL https://packages.redis.io/gpg | gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg && \
#     echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/redis.list && \
#     apt-get -y update --no-install-recommends && export DEBIAN_FRONTEND=noninteractive && \
#     apt-get -y install --no-install-recommends redis

RUN echo "vm.overcommit_memory = 1" >> /etc/sysctl.conf 


COPY --from=wheeler $NES_DIR $NES_DIR

COPY --from=wheeler /wheels /wheels

RUN pip3 install -U pip setuptools wheel && \
	pip3 install -r /wheels/requirement/requirements.txt -f /wheels && \
		rm -rf /wheels && \
		rm -rf /root/.cache/pip*


RUN sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && \
    locale-gen


RUN sed -i -r 's@ErrorLog .*@Errorlog /dev/stderr@i' /etc/apache2/apache2.conf && \
    echo "CustomLog /dev/stdout combined" >> /etc/apache2/apache2.conf && \
    sed -i -e 's/Listen 80/Listen 80\nServerName localhost/' /etc/apache2/ports.conf

# Setup certbot for automatic SSL certificates
# RUN service snap start && \
#     snap install --classic certbot && \
#     ln -s /snap/bin/certbot /usr/bin/certbot

# RUN python3 -m venv /opt/certbot/ && \
#     /opt/certbot/bin/pip install --upgrade pip && \
#     /opt/certbot/bin/pip install certbot certbot-apache && \
#     ln -s /opt/certbot/bin/certbot /usr/bin/certbot 

RUN curl -JLO "https://dl.filippo.io/mkcert/latest?for=linux/amd64" && \
    chmod +x mkcert-v*-linux-amd64 && \
    cp mkcert-v*-linux-amd64 /usr/local/bin/mkcert && \
    /usr/local/bin/mkcert -install

WORKDIR $NES_DIR

RUN cp docker/entrypoint.sh / && \
    chmod +x /entrypoint.sh 
    

ENTRYPOINT ["/entrypoint.sh"]

CMD ["/bin/bash", "-c", "service apache2 start"]

