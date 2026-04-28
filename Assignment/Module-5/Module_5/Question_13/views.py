from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from .models import Doctor
from .serializers import DoctorSerializer

# Create your views here.

def token_fetcher_view(request):
    return render(request, 'Question_13/token_fetcher.html')

def doctor_records_view(request):
    doctors = Doctor.objects.all()
    return render(request, 'Question_13/doctor_records.html', {'doctors': doctors})

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
