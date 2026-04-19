from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='q11_home'),
    path('q11_showdata/',views.showdata,name='stdata'),
]