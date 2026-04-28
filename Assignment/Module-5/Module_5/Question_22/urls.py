from django.urls import path
from . import views

urlpatterns = [
    path('map/', views.doctor_map_view, name='q22_doctor_map'),
]
