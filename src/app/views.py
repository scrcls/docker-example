# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.views.generic import View

from common.rdb import get_redis_client
from .models import *
from . import tasks

import datetime
import logging

LOGGER = logging.getLogger('app')


class JsonView(View):
    def json_ok(self, data = None, **response_kwargs):
        if data is None:
            data = {}
        result = {'data': data, 'code': 'OK'}
        return JsonResponse(result, **response_kwargs)

    def json_error(self, error, data = None, **response_kwargs):
        if data is None:
            data = {}
        result = {'error': data, 'code': error}
        return JsonResponse(result, **response_kwargs)


class HelloView(JsonView):

    def get(self, request, *args, **kwargs):
        test = Test.objects.filter().first()
        parameter = request.GET.get('parameter') or 'World'
        if not test:
            test = Test.objects.create(
                create_time = datetime.datetime.now(),
                update_time = datetime.datetime.now()
            )
        LOGGER.info('HelloView parameter:%s test:%s', parameter, test.id)
        return self.json_ok('New Hello %s:%s' % (parameter, test.id))


class CacheView(JsonView):
    KEY = 'CacheView'

    def get(self, request, *args, **kwargs):
        client = get_redis_client()
        result = client.incr(self.KEY)
        return self.json_ok('NewCacheView:%s' % result)


class TaskView(JsonView):
    KEY = 'TASK_NUM'

    def get(self, request, *args, **kwargs):
        tasks.incr_task_num.delay()
        client = get_redis_client()
        result = client.get(self.KEY)
        return self.json_ok('TaskNum:%s' % result)
