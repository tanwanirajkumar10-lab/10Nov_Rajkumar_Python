from django.shortcuts import render
from .models import Doctor


def q8_home(request):
    doctors = Doctor.objects.all()
    total = doctors.count()
    available = doctors.filter(status='available').count()
    on_leave = doctors.filter(status='on_leave').count()
    busy = doctors.filter(status='busy').count()
    context = {
        'doctors': doctors,
        'total': total,
        'available': available,
        'on_leave': on_leave,
        'busy': busy,
    }
    return render(request, 'q8_home.html', context)
