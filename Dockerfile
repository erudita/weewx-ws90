FROM debian:bookworm AS basedebian
##FROM debian:bookworm-slim AS basedebian

ARG WEEWX_UID=1001

ENV WEEWX_ROOT="/etc/weewx/" \
    USER_ROOT="/etc/weewx/bin/user" \
    WEEWX_CONF="/etc/weewx/weewx.conf" \
    HTML_ROOT="/data/public_html"

ENV WEEWX_VERSION="5.1.0" \
    MQTTSUBSCRIBE_VERSION="3.0.0" \
    MQTT_VERSION="" \
    TZ="Australia/Melbourne"

## receive (bellrichim) and send (matthewwall) through mqtt
ENV \
    MQTTSUBSCRIBE_URL="https://github.com/bellrichm/WeeWX-MQTTSubscribe/archive/refs/tags/v${MQTTSUBSCRIBE_VERSION}.zip" \
    MQTT_URL="https://github.com/matthewwall/weewx-mqtt/archive/master.zip"

LABEL org.opencontainers.image.description="MQTT version of Weewx for EcoWitt GW2000/WS90"
LABEL org.opencontainers.image.source=https://github.com/erudita/weewx-ws90
LABEL org.opencontainers.image.licence=GPL-3.0-or-later
LABEL org.opencontainers.image.authors="erudita@ankubis.com" \
      com.weewx.version=${WEEWX_VERSION}

RUN addgroup --system --gid ${WEEWX_UID} weewx && \
  adduser --system --uid ${WEEWX_UID} --ingroup weewx weewx


## required base packages
RUN apt-get update && \
    apt-get install -y wget gnupg unzip \
    tzdata rsync openssh-client openssl \
    vim-tiny \
    python3 python3-dev 

# required application dependencies
RUN apt-get install -y libffi-dev libjpeg-dev
RUN apt-get install -y python3-paho-mqtt
RUN apt-get install -y libmariadb3 python3-mysqldb
# maybe mysql-client

# configure apt for weewx
RUN wget -qO - https://weewx.com/keys.html | \
    gpg --dearmor --output /etc/apt/trusted.gpg.d/weewx.gpg

RUN wget -qO - https://weewx.com/apt/weewx-python3.list | tee /etc/apt/sources.list.d/weewx.list

RUN echo "deb [arch=all] https://weewx.com/apt/python3 buster main" | \
    tee /etc/apt/sources.list.d/weewx.list

## install weewx
RUN apt-get update && \
    apt-get install -y weewx

## install extensions
RUN weectl extension install ${MQTT_URL} --config=${WEEWX_CONF} --yes
RUN weectl extension install ${MQTTSUBSCRIBE_URL} --config=${WEEWX_CONF} --yes
WORKDIR "/tmp"
COPY bin/user/extensions.py .
WORKDIR ${USER_ROOT}
COPY bin/user/wview_extended_ws90.py .
RUN cat /tmp/extensions.py >> ${USER_ROOT}/extensions.py

WORKDIR "/"
COPY --chown=$WEEWX_UID scripts/entrypoint.sh .
ENTRYPOINT [ "/entrypoint.sh"]
CMD ["--notest"]
