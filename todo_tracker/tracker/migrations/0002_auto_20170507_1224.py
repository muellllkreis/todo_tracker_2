# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-07 10:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='todo_ptrogress',
            new_name='todo_progress',
        ),
    ]