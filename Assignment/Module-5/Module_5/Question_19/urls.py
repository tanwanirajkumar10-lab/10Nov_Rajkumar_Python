from django.urls import path
from . import views

app_name = 'Question_19'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('success/', views.registration_success_view, name='registration-success'),
]
