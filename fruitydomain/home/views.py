from django.shortcuts import render,redirect
from django.contrib import auth


def index(request):
    return render(request,'index.html')


def test(request):
    return render(request,'text.html',{'val':'java'})

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def loginsub(request):
    uname=request.GET['uname']
    pname=request.GET['pname']
    user=auth.authenticate(username=uname,password=pname)
    if user:
        auth.login(request,user)
        return redirect('/')

    return render(request,'text.html',{'val':user})

def registersub(request):
    uname=request.GET['uname']
    fname=request.GET['fname']
    lname=request.GET['lname']
    ename=request.GET['ename']
    pname=request.GET['pname']
    rpname=request.GET['rpname']
    return render(request,'text.html',{'val':uname})

    

# Create your views here.
