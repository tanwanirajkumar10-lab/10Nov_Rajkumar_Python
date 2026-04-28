from django.urls import path
from . import views

urlpatterns = [
    path('', views.country_info_view, name='country-info'),
]
