from rest_framework import viewsets
from .models import DoctorProfile
from .serializers import DoctorProfileSerializer

# Create your views here.
class DoctorProfileViewSet(viewsets.ModelViewSet):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorProfileSerializer
