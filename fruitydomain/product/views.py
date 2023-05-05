from django.shortcuts import render
from .models import fruits

def test(r):
    return render(r,'text.html')

def about(r):
    idnum=r.GET['id']
    obj=fruits.objects.get(id=idnum)
    return render(r,'about.html',{'fruit':obj})

def cmt(r):
    return render(r,'text.html')

def like(r):
    return render(r,'text.html')

# Create your views here.
