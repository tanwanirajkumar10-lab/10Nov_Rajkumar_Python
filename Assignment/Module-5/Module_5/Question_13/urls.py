from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

app_name = 'Question_13'

router = DefaultRouter()
router.register(r'doctors', views.DoctorViewSet, basename='doctor')

urlpatterns = [
    path('', include(router.urls)),
    path('fetch-token/', views.token_fetcher_view, name='token-fetcher'),
    path('records/', views.doctor_records_view, name='doctor-records'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
