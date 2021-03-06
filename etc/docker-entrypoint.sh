#!/bin/sh

set -e

HOMEDIR=/home/test
PROJECT_SRC=$HOMEDIR/src
PROJECT_ETC=$HOMEDIR/etc

cd $PROJECT_SRC

if [ "$@" == "server" ]; then
    uwsgi --ini $PROJECT_ETC/uwsgi.ini
elif [ "$@" == "cron" ]; then
    crond -f
elif [ "$@" == "celery" ]; then
    celery worker -A test -l INFO
fi

echo "$@"
exec "$@"
