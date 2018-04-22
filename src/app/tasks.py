# -*- coding:utf-8 -*-
from common.rdb import get_redis_client

from celery import shared_task

@shared_task
def incr_task_num():
    KEY = 'TASK_NUM'
    client = get_redis_client()
    return client.incr(KEY)
