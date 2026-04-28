from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login-page'),
    path('process-otp/', views.process_otp, name='process-otp'),
    path('verify-otp/', views.verify_otp, name='verify-otp'),
    path('auth-success/', views.success_view, name='success-page'),
]
