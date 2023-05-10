from django.shortcuts import render,redirect
from .models import fruits,comment


def test(r):
    return render(r,'text.html')

def about(r):
    idnum=r.GET['id']
    obj=fruits.objects.get(id=idnum)
    return render(r,'about.html',{'fruit':obj})

def cmt(r):
    imsg=r.GET["cmtmsg"]
    usname=r.GET['user']
    idpro=r.GET['id']
    obj=comment.objects.create(user=usname,msg=imsg,proid_id=idpro,like=0)
    obj.save()
    return redirect('/product/?id='+idpro)

def like(r):
    return render(r,'text.html')

# Create your views here.
