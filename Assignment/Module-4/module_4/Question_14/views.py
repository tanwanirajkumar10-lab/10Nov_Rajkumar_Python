from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from .models import doctor_profile

# Create your views here.
def home(request):
    doctors = doctor_profile.objects.all()
    return render(request,'q14_home.html', {'doctors': doctors})

def doctor_page(request):
    doctors = doctor_profile.objects.all()
    return render(request, 'doctor.html', {'doctors': doctors})


def add_doctor(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        specialization = request.POST.get('specialization')
        phone = request.POST.get('phone')

        doctor = doctor_profile.objects.create(
            name=name,
            specialization=specialization,
            phone=phone
        )

        return JsonResponse({
            'id': doctor.id,
            'name': doctor.name,
            'specialization': doctor.specialization,
            'phone': doctor.phone
        })


def edit_doctor(request, id):
    doctor = get_object_or_404(doctor_profile, id=id)

    if request.method == 'POST':
        doctor.name = request.POST.get('name')
        doctor.specialization = request.POST.get('specialization')
        doctor.phone = request.POST.get('phone')
        doctor.save()

        return JsonResponse({'status': 'updated'})


def delete_doctor(request, id):
    doctor = get_object_or_404(doctor_profile, id=id)
    doctor.delete()
    return JsonResponse({'status': 'deleted'})
