from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'writesphere'

urlpatterns = [
    # Auth
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='writesphere:home'), name='logout'),
    
    # Blog Posts
    path('', views.PostListView.as_view(), name='home'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<slug:slug>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<slug:slug>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    
    # Interactions
    path('post/<slug:slug>/comment/', views.CommentCreateView.as_view(), name='post_comment'),
    path('post/<slug:slug>/like/', views.LikeToggleView.as_view(), name='post_like'),
    path('author/<str:username>/follow/', views.FollowToggleView.as_view(), name='author_follow'),
    path('category/<slug:slug>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),
]
