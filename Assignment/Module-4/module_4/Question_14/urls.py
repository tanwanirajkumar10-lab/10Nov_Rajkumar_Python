from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='q14_home'),
    path('add/', views.add_doctor, name='add_doctor'),
    path('edit/<int:id>/', views.edit_doctor, name='edit_doctor'),
    path('delete/<int:id>/', views.delete_doctor, name='delete_doctor'),

]
