# -*- coding:utf-8 -*-
from django.conf import settings

from redis import StrictRedis
from redis.connection import ConnectionPool

_REDIS = None

def get_redis_client():
    global _REDIS
    if not _REDIS:
        _REDIS = StrictRedis(connection_pool = ConnectionPool(**settings.REDIS_CONFIG))
    return _REDIS
