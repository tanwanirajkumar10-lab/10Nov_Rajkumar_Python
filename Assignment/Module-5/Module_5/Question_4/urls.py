from django.urls import path
from . import views

urlpatterns = [
    path('add-doctor/', views.DoctorCreateView.as_view(), name='add-doctor'),
]
