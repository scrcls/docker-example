FROM python:2.7-alpine

RUN addgroup -S django && adduser -S -G django django
RUN mkdir /workspace && chown django:django /workspace

WORKDIR /workspace

COPY requirements.txt /workspace/
RUN set -ex ; \
    apk add --no-cache --virtual .BUILD_DEPS \
        gcc \
        musl-dev \
        python-dev \
        mariadb-dev \
    ; \
    pip install -U pip; \
    pip install -r requirements.txt;
    # apk del .BUILD_DEPS; 

COPY . /workspace
