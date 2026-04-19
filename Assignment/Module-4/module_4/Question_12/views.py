from django.shortcuts import render,redirect
from .forms import *

# Create your views here.
def home(request):
    if request.method=='POST':
        form=DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            print("Record Inserted!")
        else:
            print(form.errors)
    return render(request,'q12_home.html')

def showdata(request):
    stdata=doctorprofile.objects.all()
    return render(request,'q12_showdata.html',{'stdata':stdata})


def updatedata(request,id):
    stid=doctorprofile.objects.get(id=id)
    if request.method=='POST':
        form=DoctorForm(request.POST,instance=stid)
        if form.is_valid():
            form.save()
            print("Record Updated!")
            return redirect('showdata')
        else:
            print(form.errors)
    return render(request,'q12_updatedata.html',{'stid':stid})


def deletedata(request,id):
    stid=doctorprofile.objects.get(id=id)
    doctorprofile.delete(stid)
    return redirect('showdata')