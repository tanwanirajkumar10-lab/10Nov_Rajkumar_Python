from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctor_list, name='q15_home'),
]
