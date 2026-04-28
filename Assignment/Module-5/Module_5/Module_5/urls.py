"""
URL configuration for module_4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_app.urls')),
    path('q1/', include('Question_1.urls')),
    path('q2/', include('Question_2.urls')),
    path('q3/', include('Question_3.urls')),
    path('q4/', include('Question_4.urls')),
    path('q5/', include('Question_5.urls')),
    path('q6/', include('Question_6.urls')),
    path('q7/', include('Question_7.urls')),
    path('q8/', include('Question_8.urls')),
    path('doctor-finder/', include('doctor_finder.urls')),
    path('q10/', include('Question_10.urls')),
    path('q11/', include('Question_11.urls')),
    path('q12/', include('Question_12.urls')),
    path('q13/', include('Question_13.urls')),
    path('q14/', include('Question_14.urls')),
    path('q15/', include('Question_15.urls')),
    path('q16/', include('Question_16.urls')),
    path('q17/', include('Question_17.urls')),
    path('q18/', include('Question_18.urls')),
    path('q19/', include('Question_19.urls')),
    path('q20/', include('Question_20.urls')),
    path('q21/', include('Question_21.urls')),
    path('q22/', include('Question_22.urls')),
    path('accounts/', include('allauth.urls')),
]
