FROM python:3.9-buster


ARG APP_DIR=/app
ARG APP_USER=appuser

RUN groupadd -r ${APP_USER} && \
    useradd --no-create-home -u 1000 -r -g ${APP_USER} ${APP_USER}

COPY --chown=${APP_USER}:${APP_USER} wait-for.sh requirements.txt service/ ${APP_DIR}/

RUN apt-get update && \
    apt-get install --yes --no-install-recommends \
        postgresql-client \
        musl-dev \
        gcc \
        vim \
        netcat \
        gettext \
        libgettextpo-dev && \
    pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r ${APP_DIR}/requirements.txt && \
    chmod a+x ${APP_DIR}/wait-for.sh && \
    chown -R ${APP_USER}:${APP_USER} ${APP_DIR} && \
    rm -rf /var/lib/apt/lists/*

WORKDIR ${APP_DIR}

USER ${APP_USER}:${APP_USER}
