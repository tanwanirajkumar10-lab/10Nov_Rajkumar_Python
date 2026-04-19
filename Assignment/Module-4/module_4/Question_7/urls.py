from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='q7_home'),
    path('q7_showdata/',views.showdata,name='stdata'),
]