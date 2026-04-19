from django.shortcuts import render

from .models import Doctor

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'Question_15/q15_home.html', {'doctors': doctors})
