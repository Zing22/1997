# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-29 14:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='time_slot',
            field=models.TextField(default='[]', max_length=4096),
        ),
    ]