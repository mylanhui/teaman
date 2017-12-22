# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-22 14:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teaManSys', '0004_auto_20171222_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='coursesId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teaManSys.courses'),
        ),
        migrations.AlterField(
            model_name='student',
            name='coursesId',
            field=models.ManyToManyField(to='teaManSys.courses'),
        ),
    ]