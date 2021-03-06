# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-22 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teaManSys', '0002_auto_20171222_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='coursesId',
            field=models.CharField(max_length=8, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='studentId',
            field=models.CharField(max_length=12, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacherId',
            field=models.CharField(max_length=8, primary_key=True, serialize=False),
        ),
    ]
