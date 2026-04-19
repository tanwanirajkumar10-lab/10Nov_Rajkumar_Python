from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='q9_home'),
    path('q9_profile/', views.profile),
    path('q9_contact/', views.contact),

]