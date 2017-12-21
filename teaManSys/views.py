from django.http import HttpResponse
from django.shortcuts import render, render_to_response


# Create your views here.
def model(req):

    return render_to_response('model.html')

def signIn(req):
    return render_to_response('login/sign-in.html')

def signup(req):
    return render_to_response('login/sign-up.html')


def grade(req):
    return render_to_response('page/grade.html')

def teacher(req):
    return render_to_response('page/teacher.html')

def student(req):
    return render_to_response('page/student.html')

def classa(req):
    return render_to_response('page/class.html')

def courses(req):
    return render_to_response('page/courses.html')