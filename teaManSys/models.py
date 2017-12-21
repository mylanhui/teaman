from __future__ import unicode_literals

from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()

class classList(models.Model):
    classId = models.AutoField(primary_key=True)
    className = models.CharField(max_length=12)
    college = models.CharField (max_length=20)
    major = models.CharField(max_length=20)
    studentNum = models.IntegerField()

class student(models.Model):
    studentId = models.AutoField(primary_key=True)
    studentName = models.CharField(max_length=10)
    birthday = models.DateTimeField()
    studentCourses = models.IntegerField()
    classId = models.ForeignKey(classList,db_column="classId")
    studentSex = models.BooleanField(default=0)

class teacher(models.Model):
    teacherId = models.AutoField(primary_key=True)
    teacherName = models.CharField(max_length=10)
    teacherSex = models.BooleanField(default=0)
    teacherTitle = models.CharField(max_length=20)


class courses(models.Model):
    coursesId =models.AutoField(primary_key=True)
    coursesName =models.CharField(max_length=40)
    coursesTime =models.CharField(max_length=20)
    credit =models.IntegerField()
    teacherId =models.ForeignKey(teacher,db_column="teacherId")
    studentId =models.ManyToManyField(student,db_column="studentId")


class grade(models.Model):
    gradeId = models.AutoField(primary_key=True)
    studentId =models.ForeignKey(student,db_column="studentId")
    coursesId =models.ForeignKey(courses,db_column="coursesId")
    score =models.CharField(max_length=10)


class user(models.Model):
    userId =models.AutoField(primary_key=True)
    password =models.CharField(max_length=16)



