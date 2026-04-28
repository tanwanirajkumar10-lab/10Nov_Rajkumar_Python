from rest_framework import generics
from .models import Doctor
from .serializers import DoctorSerializer

# Create your views here.
class DoctorCreateView(generics.CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
