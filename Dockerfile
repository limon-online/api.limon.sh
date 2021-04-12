FROM python:3.10-rc-buster


ARG APP_DIR=/app
ARG APP_USER=appuser

RUN groupadd -r ${APP_USER} && \
    useradd --no-create-home -u 1000 -r -g ${APP_USER} ${APP_USER}

COPY --chown=${APP_USER}:${APP_USER} requirements.txt service/ ${APP_DIR}/

RUN apt-get update && \
    apt-get install --yes --no-install-recommends \
        postgresql-client \
        musl-dev \
        gcc \
        gettext \
        libgettextpo-dev && \
    pip3 install --no-cache-dir -r ${APP_DIR}/requirements.txt && \
    chown -R ${APP_USER}:${APP_USER} ${APP_DIR} && \
    rm -rf /var/lib/apt/lists/*

WORKDIR ${APP_DIR}

USER ${APP_USER}:${APP_USER}
