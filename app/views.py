# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.views.generic import View


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
        return self.json_ok('Hello World')
