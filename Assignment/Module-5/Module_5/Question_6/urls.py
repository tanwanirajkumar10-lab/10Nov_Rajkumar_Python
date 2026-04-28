from django.urls import path
from . import views

urlpatterns = [
    path('doctors/', views.DoctorListCreateView.as_view(), name='doctor-list-create-custom'),
    path('doctors/<int:pk>/', views.DoctorRetrieveUpdateDestroyView.as_view(), name='doctor-detail-custom'),
]
