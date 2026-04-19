from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='q12_home'),
    path('q12_showdata/',views.showdata,name='showdata'),
    path('q12_updatedata/<int:id>',views.updatedata),
    path('q12_deletedata/<int:id>',views.deletedata,name='deletedata'),
]
