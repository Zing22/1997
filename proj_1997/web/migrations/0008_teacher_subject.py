# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-02 02:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_teacher_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='subject',
            field=models.CharField(default='', max_length=1024),
            preserve_default=False,
        ),
    ]
