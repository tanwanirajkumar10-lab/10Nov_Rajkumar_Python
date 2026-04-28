from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import Doctor
from .serializers import DoctorSerializer

# Custom Pagination class
class DoctorPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

# Create your views here.
class DoctorListView(generics.ListAPIView):
    queryset = Doctor.objects.all().order_by('id')
    serializer_class = DoctorSerializer
    pagination_class = DoctorPagination
