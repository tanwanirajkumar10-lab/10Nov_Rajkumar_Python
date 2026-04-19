from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout

# Create your views here.

def home(request):
    user=request.session.get("user")
    return render(request,'q13_home.html',{'user':user})


def login(request):
    if request.method=='POST':
        em=request.POST['email']
        pa=request.POST['password']
        
        user=userSignup.objects.filter(email=em,password=pa)
        if user:
            print("Login Successfully!")
            request.session["user"]=em
            return redirect('q13_home')
        else:
            print("Error!")    
    return render(request,'q13_login.html')

def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            print("Signup Successfully!")
            return redirect('/')
        else:
            print(form.errors)
    return render(request,'q13_signup.html')

def showprofile(request):
    email = request.session.get('user')

    if not email:
        return redirect('/q13')

    stdata = userSignup.objects.filter(email=email).first()

    if not stdata:
        return redirect('/q13')

    return render(request, 'q13_showprofile.html', {'stdata': stdata})


def updateprofile(request,id):
    stid=userSignup.objects.get(id=id)
    if request.method=='POST':
        form=SignupForm(request.POST,instance=stid)
        if form.is_valid():
            form.save()
            print("Record Updated!")
            return redirect('q13_showprofile')
        else:
            print(form.errors)
    return render(request,'q13_updateprofile.html',{'stid':stid})

def reset_password(request):
    email = request.session.get('user')

    if not email:
        return redirect('/q13')

    user = userSignup.objects.filter(email=email).first()

    if not user:
        return redirect('/q13')

    if request.method == 'POST':
        new_password = request.POST.get('password')

        if new_password:
            user.password = new_password
            user.save()
            return redirect('q13_showprofile')

    return render(request, 'q13_resetpassword.html')

def userlogout(request):
    request.session.flush()
    return redirect('/q13')

