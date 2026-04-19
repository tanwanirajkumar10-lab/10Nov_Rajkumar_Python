from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'q5_home.html')