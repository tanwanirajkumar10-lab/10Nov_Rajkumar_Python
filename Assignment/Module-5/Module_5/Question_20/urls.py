from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_with_otp, name='q20_register'),
    path('verify-otp/', views.verify_otp, name='q20_verify_otp'),
]
