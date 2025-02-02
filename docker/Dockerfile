FROM python:3.11-slim-bookworm AS wheeler

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV DEBIAN_FRONTEND=noninteractive

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8


ARG NES_BRANCH
ENV NES_BRANCH=jupyter
ENV NES_DIR=/usr/local/nes


RUN apt-get update -q -y && apt-get install -y --no-install-recommends \
    python3-dev \
    libjpeg-dev \
    libpng-dev \
    libpq-dev \
    libfreetype6-dev \
    zlib1g-dev \
    g++ \
    make \
    git && \
    apt-get autoremove -y && \
    apt-get clean -y && \
    rm -rf /var/lib/apt-get/lists/* && \
    ln -s /usr/include/locale.h /usr/include/xlocale.h


RUN mkdir -p "$NES_DIR"  && \
    if [ "$NES_BRANCH" ]; then \
    echo Cloning "$NES_BRANCH "branch ;\
    git clone -j $(nproc) -b "$NES_BRANCH"  https://github.com/mcostat/nes.git "$NES_DIR" ;\
    else \
    echo Cloning master branch ;\
    git clone -j $(nproc) https://github.com/mcostat/nes.git "$NES_DIR" ;\
    fi


RUN mkdir -p /wheels/requirement && \
    cp "$NES_DIR"/patientregistrationsystem/qdc/requirements.txt /wheels/requirement

WORKDIR /wheels

RUN pip3 --no-cache-dir --disable-pip-version-check install -U pip setuptools wheel && \
    pip3 --no-cache-dir --disable-pip-version-check install -r requirement/requirements.txt && \
    pip3 wheel -r requirement/requirements.txt


FROM python:3.11-slim-bookworm

ENV PYTHONUNBUFFERED=1
ENV PYTHONOPTIMIZE=1

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

ENV NES_DIR=/usr/local/nes

ENV USERNAME=nes
ARG USER_UID=1000
ARG USER_GID=$USER_UID


RUN apt-get update -q -y && apt-get install -y --no-install-recommends \
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
    rm -rf /var/lib/apt-get/lists/* && \
    ln -s /usr/include/locale.h /usr/include/xlocale.h


RUN echo "vm.overcommit_memory = 1" >> /etc/sysctl.conf


COPY --from=wheeler ${NES_DIR} ${NES_DIR}

COPY --from=wheeler /wheels /wheels


RUN groupadd --gid "$USER_GID" "$USERNAME" \
    && useradd --uid "$USER_UID" --gid "$USER_GID" -m "$USERNAME" \
    && apt-get update \
    && apt-get install -y sudo \
    && echo "$USERNAME" ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/"$USERNAME" \
    && chmod 0440 /etc/sudoers.d/"$USERNAME" \
    && chown -R "$USERNAME" "$NES_DIR" \
    && chmod 755 "$NES_DIR"


RUN pip3 --no-cache-dir --disable-pip-version-check install -U pip setuptools wheel && \
    pip3 --no-cache-dir --disable-pip-version-check install -r /wheels/requirement/requirements.txt -f /wheels && \
    rm -rf /wheels && \
    rm -rf /root/.cache/pip*


RUN sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && \
    locale-gen


RUN sed -i -r 's@ErrorLog .*@Errorlog /dev/stderr@i' /etc/apache2/apache2.conf && \
    echo "CustomLog /dev/stdout combined" >> /etc/apache2/apache2.conf && \
    sed -i -e 's/Listen 80/Listen 80\nServerName localhost/' /etc/apache2/ports.conf

# Setup certbot for automatic SSL certificates (does not work on localhost)
# RUN python3 -m venv /opt/certbot/ && \
#     /opt/certbot/bin/pip install --upgrade pip && \
#     /opt/certbot/bin/pip install certbot certbot-apache && \
#     ln -s /opt/certbot/bin/certbot /usr/bin/certbot

RUN curl -JLO "https://dl.filippo.io/mkcert/latest?for=linux/amd64" && \
    chmod +x mkcert-v*-linux-amd64 && \
    cp mkcert-v*-linux-amd64 /usr/local/bin/mkcert && \
    /usr/local/bin/mkcert -install

COPY docker/.env $NES_DIR/patientregistrationsystem/qdc

COPY docker/entrypoint.sh /
RUN chmod +x /entrypoint.sh


WORKDIR ${NES_DIR}
#USER ${USERNAME}


ENTRYPOINT ["/entrypoint.sh"]

CMD ["/bin/bash", "-c", "service apache2 start"]
