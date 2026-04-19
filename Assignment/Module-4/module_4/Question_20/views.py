from django.shortcuts import render
from .models import DoctorLocation

def doctor_map_view(request):
    doctors = DoctorLocation.objects.all()
    return render(request, 'Question_20/map.html', {'doctors': doctors})
