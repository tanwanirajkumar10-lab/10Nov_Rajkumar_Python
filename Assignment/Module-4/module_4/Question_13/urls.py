from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.login),
    path('q13_signup/', views.signup, name='q13_signup'),
    path('q13_home/', views.home, name='q13_home'),
    path('q13_showprofile/', views.showprofile, name='q13_showprofile'),
    path('q13_updateprofile/<int:id>',views.updateprofile, name='q13_updateprofile'),
    path('q13_resetpassword/', views.reset_password, name='q13_resetpassword'),
    path('q13_userlogout/',views.userlogout, name='q13_userlogout'),
]
