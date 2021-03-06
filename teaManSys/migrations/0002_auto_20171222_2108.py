# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-22 13:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teaManSys', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='classList',
            fields=[
                ('classId', models.AutoField(primary_key=True, serialize=False)),
                ('className', models.CharField(max_length=12)),
                ('studentNum', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='college',
            fields=[
                ('collegeId', models.AutoField(primary_key=True, serialize=False)),
                ('collegeName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='courses',
            fields=[
                ('coursesId', models.AutoField(primary_key=True, serialize=False)),
                ('coursesName', models.CharField(max_length=40)),
                ('coursesTime', models.CharField(max_length=20)),
                ('credit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='grade',
            fields=[
                ('gradeId', models.AutoField(primary_key=True, serialize=False)),
                ('score', models.CharField(max_length=10)),
                ('coursesId', models.ForeignKey(db_column='coursesId', on_delete=django.db.models.deletion.CASCADE, to='teaManSys.courses')),
            ],
        ),
        migrations.CreateModel(
            name='major',
            fields=[
                ('majorId', models.AutoField(primary_key=True, serialize=False)),
                ('majorName', models.CharField(max_length=50)),
                ('collegeId', models.ForeignKey(db_column='collegeId', on_delete=django.db.models.deletion.CASCADE, to='teaManSys.college')),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('studentId', models.AutoField(primary_key=True, serialize=False)),
                ('studentName', models.CharField(max_length=10)),
                ('studentCourses', models.IntegerField()),
                ('studentSex', models.BooleanField(default=0)),
                ('classId', models.ForeignKey(db_column='classId', on_delete=django.db.models.deletion.CASCADE, to='teaManSys.classList')),
                ('collegeId', models.ForeignKey(db_column='collegeId', on_delete=django.db.models.deletion.CASCADE, to='teaManSys.college')),
                ('majorId', models.ForeignKey(db_column='majorId', on_delete=django.db.models.deletion.CASCADE, to='teaManSys.major')),
            ],
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('teacherId', models.AutoField(primary_key=True, serialize=False)),
                ('teacherName', models.CharField(max_length=10)),
                ('teacherSex', models.BooleanField(default=0)),
                ('teacherTitle', models.CharField(max_length=20)),
                ('collegeId', models.ForeignKey(db_column='collegeId', on_delete=django.db.models.deletion.CASCADE, to='teaManSys.college')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userId', models.AutoField(primary_key=True, serialize=False)),
                ('uerName', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=16)),
            ],
        ),
        migrations.DeleteModel(
            name='BlogPost',
        ),
        migrations.AddField(
            model_name='grade',
            name='studentId',
            field=models.ForeignKey(db_column='studentId', on_delete=django.db.models.deletion.CASCADE, to='teaManSys.student'),
        ),
        migrations.AddField(
            model_name='courses',
            name='studentId',
            field=models.ManyToManyField(db_column='studentId', to='teaManSys.student'),
        ),
        migrations.AddField(
            model_name='courses',
            name='teacherId',
            field=models.ForeignKey(db_column='teacherId', on_delete=django.db.models.deletion.CASCADE, to='teaManSys.teacher'),
        ),
        migrations.AddField(
            model_name='classlist',
            name='collegeId',
            field=models.ForeignKey(db_column='collegeId', on_delete=django.db.models.deletion.CASCADE, to='teaManSys.college'),
        ),
        migrations.AddField(
            model_name='classlist',
            name='majorId',
            field=models.ForeignKey(db_column='majorId', on_delete=django.db.models.deletion.CASCADE, to='teaManSys.major'),
        ),
    ]
