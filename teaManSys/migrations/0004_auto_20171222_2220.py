# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-22 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teaManSys', '0003_auto_20171222_2202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='studentId',
        ),
        migrations.AddField(
            model_name='student',
            name='coursesId',
            field=models.ManyToManyField(db_column='coursesId', to='teaManSys.courses'),
        ),
    ]
