import re
from django.shortcuts import render, redirect

# Create your views here.
from admins.models import UploadModel
from user.models import RegisterModel, PhishingModel


def index(request):
    pawd=''
    usname=''
    li=''
    ans=''
    cl=[]
    serh=[]
    prm=[]
    splt=''
    if request.method=="POST":
        usname=request.POST.get('username')
        pawd=request.POST.get('password')
        try:

            check = RegisterModel.objects.get(userid=usname, password=pawd)
            request.session['userid'] = check.id
            return redirect('userpage')
        except:
            splt=(re.findall(r"[\w']+", str(usname)))
            for a in splt:
                if a in ('http'):
                    serh.append(a)
                elif a in ('com','in','info','edu'):
                    prm.append(a)
                else:
                    li = list(usname)
                    for f in li:

                        if f in ('0', '1','2','3','4','5','6','8','9'):
                            cl.append(f)
                        else:
                            ans = 'Whaling Phishing Attack'




            if len(cl):
                ans='Spear Phishing Attack'
            elif len(prm) :
                ans='Pharming Phishing Attack'
            elif len(serh):
                ans=' Search Engine Phishing Attack'
    PhishingModel.objects.create(attack_type=ans, text=usname)






    return render(request,'user/index.html',{'a':ans,'b':usname})

def register(request):
    a=''
    b=''
    c=''
    d=''
    e=''
    f=''
    g=''

    if request.method=="POST":
        a=request.POST.get('fname')
        b=request.POST.get('lname')
        c=request.POST.get('userid')
        d=request.POST.get('pword')
        e=request.POST.get('mblenum')
        f=request.POST.get('email')
        g=request.POST.get('gender')
        RegisterModel.objects.create(firstname=a,lastname=b,userid=c,password=d,mblenum=e,email=f,gender=g)

    return render(request,'user/register.html',{'a':a,'b':b,'c':c,'d':d,'e':e,'f':f,'g':g})

def userpage(request):
    obj=UploadModel.objects.all()
    return render(request,'user/userpage.html',{'obj':obj})

def mydetails(request):
    usid = request.session['userid']
    us_id = RegisterModel.objects.get(id=usid)
    return render(request,'user/mydetails.html',{'obje':us_id})