from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from product.models import fruits


def index(request):
    obj=fruits.objects.all()
    print('hi',obj)
    return render(request,'index.html',{'data':obj})



def test(request):
    return render(request,'text.html',{'val':'java'})




def login(request):
    if request.method=='POST':
        uname=request.POST['uname']
        pname=request.POST['pname']
        user=auth.authenticate(username=uname,password=pname)
        if user:
            auth.login(request,user)
            return redirect('/')
        msg= "invalid username and password"

        return render(request,'login.html',{'msg':msg})
    else:
         return render(request,'login.html')


def register(request):
    if request.method=='POST':
        uname=request.POST['uname']
        fname=request.POST['fname']
        lname=request.POST['lname']
        ename=request.POST['ename']
        pname=request.POST['pname']
        rpname=request.POST['rpname']
        if pname ==rpname:
            if User.objects.filter(username=uname):
                msg='username is already taken'
                return render(request,'register.html',{'msg':msg})
            elif User.objects.filter(email=ename):
                msg='email is already registered'
                return render(request,'register.html',{'msg':msg})
            else:
                user=User.objects.create_user(first_name=fname,last_name=lname,password=pname,username=uname,email=ename)
                user.save();
                auth.login(request,user)

                return redirect('/')
        else:
            msg="password do not match"
            return render(request,'register.html',{'msg':msg})
    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

    

# Create your views here.
