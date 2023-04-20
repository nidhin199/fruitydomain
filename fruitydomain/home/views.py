from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User


def index(request):
    return render(request,'index.html')


def test(request):
    return render(request,'text.html',{'val':'java'})

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def loginsub(request):
    uname=request.POST['uname']
    pname=request.POST['pname']
    user=auth.authenticate(username=uname,password=pname)
    if user:
        auth.login(request,user)
        return redirect('/')

    return render(request,'login.html')

def registersub(request):
    uname=request.POST['uname']
    fname=request.POST['fname']
    lname=request.POST['lname']
    ename=request.POST['ename']
    pname=request.POST['pname']
    rpname=request.POST['rpname']
    if pname ==rpname:
        if User.objects.filter(username=uname):
            msg='username is already taken'
            return render(request,'text.html',{'val':msg})
        elif User.objects.filter(email=ename):
            msg='email is already registered'
            return render(request,'text.html',{'val':msg})
        else:
            user=User.objects.create_user(first_name=fname,last_name=lname,password=pname,username=uname,email=ename)
            user.save();

            return redirect('/')
    else:
        msg="password do not match"


        return render(request,'text.html',{'val':msg})

    

# Create your views here.
