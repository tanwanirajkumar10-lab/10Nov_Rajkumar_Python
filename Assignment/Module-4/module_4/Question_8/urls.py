from django.urls import path
from . import views

urlpatterns = [
    path('', views.q8_home, name='q8_home'),
]
