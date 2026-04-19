from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'q9_home.html')

def profile(request):
    return render(request,'q9_profile.html')

def contact(request):
    return render(request,'q9_contact.html')