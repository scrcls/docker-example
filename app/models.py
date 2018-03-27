# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Test(models.Model):

    create_time = models.DateTimeField('创建时间')
    update_time = models.DateTimeField('更新时间')
