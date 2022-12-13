from django.db.models import Count
from django.shortcuts import render, redirect


# Create your views here.
from admins.forms import UploadForm
from admins.models import UploadModel
from user.models import RegisterModel, PhishingModel


def admins(request):
    if request.method == "POST":
        if request.method == "POST":
            usid = request.POST.get('username')
            pswd = request.POST.get('password')
            if usid == 'admin' and pswd == 'admin':
                return redirect('admin_page')
    return render(request,'admins/admins.html')

def admin_page(request):
    if request.method=="POST":
        forms=UploadForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('admin_page')
    else:
        forms = UploadForm()
    return render(request,'admins/admin_page.html',{'form':forms})

def user_details(request):
    obj = RegisterModel.objects.all()
    return render(request,'admins/user_details.html',{'objects':obj})

def attack_details(request):
    obj=PhishingModel.objects.all()
    return render(request,'admins/attack_details.html',{'obj':obj})

def chart_page(request):
    chart = PhishingModel.objects.values('attack_type').annotate(dcount=Count('attack_type'))
    return render(request,'admins/chart_page.html',{'obj':chart})