# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-08 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20170507_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='todo_date',
            field=models.CharField(max_length=40),
        ),
    ]