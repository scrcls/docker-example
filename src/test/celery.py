# -*- coding:utf-8 -*-
from __future__ import absolute_import

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test.settings')

from celery import Celery
from django.conf import settings

app = Celery('test')
app.config_from_object(settings.CELERY_CONFIG)
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
