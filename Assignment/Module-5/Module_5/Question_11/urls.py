from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet

app_name = 'Question_11'

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet, basename='doctor')

urlpatterns = [
    path('', include(router.urls)),
]
