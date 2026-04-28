from django.urls import path
from . import views

urlpatterns = [
    path('', views.q2_home, name='q2_home'),
]
