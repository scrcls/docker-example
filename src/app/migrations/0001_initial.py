# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-27 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(verbose_name='\u66f4\u65b0\u65f6\u95f4')),
            ],
        ),
    ]
