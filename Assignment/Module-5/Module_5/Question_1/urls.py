from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='q1_home'),
    path('joke/', views.JokeView.as_view(), name='random_joke'),
]