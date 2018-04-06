FROM python:2.7-alpine as dev

ENV TZ Asia/Hong_Kong
ENV LANG C.UTF-8
ENV USER test
ENV HOMEDIR /home/test/
ENV PROJECT_SRC /home/test/src
ENV PROJECT_ETC /home/test/etc
ENV PROJECT_VAR /home/test/var

RUN addgroup -S $USER && adduser -S -G $USER $USER
RUN set -ex ; \
    mkdir $HOMEDIR && chown $USER:$USER $HOMEDIR; \
    mkdir $PROJECT_SRC && chown $USER:$USER $PROJECT_SRC; \
    mkdir $PROJECT_ETC && chown $USER:$USER $PROJECT_ETC; \
    mkdir $PROJECT_VAR && chown $USER:$USER $PROJECT_VAR;

COPY requirements.txt $HOMEDIR
RUN set -ex ; \
    apk add --no-cache --virtual .BUILD_DEPS \
        gcc \
        build-base \
    ; \
    apk add --no-cache \
        musl-dev \
        python-dev \
        mariadb-dev \
        linux-headers \
    ; \
    pip install -U pip; \
    pip install -r $HOMEDIR/requirements.txt; \
    pip install -U --no-cache-dir uWSGI==2.0.17; \
    apk del .BUILD_DEPS;

WORKDIR $PROJECT_SRC
COPY ./src $PROJECT_SRC
COPY ./etc/uwsgi.ini $PROJECT_ETC/uwsgi.ini

COPY ./etc/docker-entrypoint.sh /usr/local/bin/
ENTRYPOINT ["docker-entrypoint.sh"]

CMD ["server"]

# EXPOSE 8080
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]

