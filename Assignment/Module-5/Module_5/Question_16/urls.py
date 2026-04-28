from django.urls import path
from . import views

app_name = 'Question_16'

urlpatterns = [
    path('', views.github_dashboard_view, name='github-dashboard'),
    path('create/', views.create_repo_action, name='create-repo'),
]
