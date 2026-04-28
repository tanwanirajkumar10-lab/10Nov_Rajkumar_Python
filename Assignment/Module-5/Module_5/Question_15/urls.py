from django.urls import path
from . import views

urlpatterns = [
    path('', views.geocode_view, name='geocode-view'),
]
