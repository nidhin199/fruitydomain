from django.shortcuts import render,redirect
from .models import fruits,comment


def test(r):
    return render(r,'text.html')

def about(r):
    idnum=r.GET['id']
    obj=fruits.objects.get(id=idnum)
    if 'recent' in r.session:
        if idnum in r.session['recent']:
            r.session['recent'].remove(idnum)
        data=fruits.objects.filter(id__in=r.session['recent'])
        r.session['recent'].insert(0,idnum )
        if len(r.session['recent'])>=5:
            r.session['recent'].pop()
    else:
        r.session['recent']=[idnum]
        data=[]
    r.session.modified=True   
    return render(r,'about.html',{'fruit':obj,'rec':data})

def cmt(r):
    imsg=r.GET["cmtmsg"]
    usname=r.GET['user']
    idpro=r.GET['id']
    obj=comment.objects.create(user=usname,msg=imsg,proid_id=idpro,like=0)
    obj.save()
    return redirect('/product/?id='+idpro)

def like(r):
    cmtid=r.GET['id']
    obj=comment.objects.filter(id=cmtid)
    like=int(obj[0].like)+1
    obj.update(like=str(like))
    return redirect('/product/?id='+str(obj[0].proid_id))

# Create your views here.
