from django.http import HttpResponse
from django.shortcuts import render, render_to_response


# Create your views here.
def model(req):

    return render_to_response('model.html')

def signIn(req):
    return render_to_response('login/sign-in.html')

def signup(req):
    return render_to_response('login/sign-up.html')


def index(req):
    return render_to_response('page/index.html')