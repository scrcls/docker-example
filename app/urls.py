# -*- coding:utf-8 -*-
from django.conf.urls import include, url

from .views import *

urlpatterns = [
    url('^hello/$', HelloView.as_view(), name = 'hello_view'),
]
