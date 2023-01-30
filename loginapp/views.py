from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse



def welcome(req):
    return render(req,'welcome.html')


def login(req):
    return render(req,'login.html')

def contact(request):
    return render(request,'contact us.html')

def register(req):
    return render(req,'register.html')   
     








#