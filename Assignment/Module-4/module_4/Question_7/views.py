from django.shortcuts import render
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
    return render(request,'q7_home.html')

def showdata(request):
    stdata=doctorinfo.objects.all()
    return render(request,'q7_showdata.html',{'stdata':stdata})