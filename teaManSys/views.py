from django.http import HttpResponse
from django.shortcuts import render, render_to_response


# Create your views here.
from teaManSys import models


def model(req):

    return render_to_response('model.html')

def signIn(req):
    return render_to_response('login/sign-in.html')

def signup(req):
    if req.method == 'POST':
        userName = req.POST["userName"]
        user = models.User.objects.filter(userName=userName)
        if user.count() > 0:
            return HttpResponse(2)
        passWord = req.POST["passWord"]
        yanzhengma = req.POST['Input_verify']
        if req.COOKIES.get('validate', '').upper() != yanzhengma.upper():
            return HttpResponse(3)
        userId = uuid.uuid1()
        try:
            userSave = models.User(userId=userId, userName=userName, userPwd=passWord)
            userSave.save()
            return HttpResponse(1)
        except Exception as err:
            return HttpResponse(0)
    else:
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