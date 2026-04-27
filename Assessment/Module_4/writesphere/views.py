from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import login
from django.db.models import Q
from django.http import HttpResponseRedirect

from .models import Post, Comment, Like, Follow, User, Category
from .forms import UserRegistrationForm, PostForm, CommentForm

class RegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'writesphere/register.html'
    success_url = reverse_lazy('writesphere:home')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.role = 'author' # Default role for new signups
        user.save()
        login(self.request, user)
        return super().form_valid(form)

class CustomLoginView(LoginView):
    template_name = 'writesphere/login.html'
    
    def get_success_url(self):
        return reverse_lazy('writesphere:home')

class PostListView(ListView):
    model = Post
    template_name = 'writesphere/home.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = Post.objects.all().select_related('author').prefetch_related('categories')
        
        # Filtering by category
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(categories__slug=category)
            
        # Filtering by author
        author = self.request.GET.get('author')
        if author:
            queryset = queryset.filter(author__username=author)
            
        # Search
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) | Q(content__icontains=q)
            )
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'writesphere/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['comments'] = self.object.comments.all().select_related('author')
        
        # Like status
        context['has_liked'] = False
        if self.request.user.is_authenticated:
            context['has_liked'] = Like.objects.filter(user=self.request.user, post=self.object).exists()
            
        # Follow status
        context['is_following'] = False
        if self.request.user.is_authenticated and self.request.user != self.object.author:
            context['is_following'] = Follow.objects.filter(follower=self.request.user, following=self.object.author).exists()
            
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'writesphere/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        self.object = form.save(user=self.request.user)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('writesphere:post_detail', kwargs={'slug': self.object.slug})

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'writesphere/post_form.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author or self.request.user.role == 'admin'

    def form_valid(self, form):
        self.object = form.save(user=self.request.user)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('writesphere:post_detail', kwargs={'slug': self.object.slug})

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'writesphere/post_confirm_delete.html'
    success_url = reverse_lazy('writesphere:home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author or self.request.user.role == 'admin'

class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
        return HttpResponseRedirect(reverse('writesphere:post_detail', args=[slug]))

class LikeToggleView(LoginRequiredMixin, View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if not created:
            like.delete()
        return HttpResponseRedirect(reverse('writesphere:post_detail', args=[slug]))

class FollowToggleView(LoginRequiredMixin, View):
    def post(self, request, username, *args, **kwargs):
        author = get_object_or_404(User, username=username)
        if request.user != author:
            follow, created = Follow.objects.get_or_create(follower=request.user, following=author)
            if not created:
                follow.delete()
        
        # Redirect back to where they came from
        next_url = request.POST.get('next') or request.META.get('HTTP_REFERER') or reverse('writesphere:home')
        return HttpResponseRedirect(next_url)

class CategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('writesphere:home')

    def test_func(self):
        category = self.get_object()
        # Allow if: creator is NULL (legacy category), user is creator, or user is admin/superuser
        return (
            category.creator is None
            or category.creator == self.request.user
            or self.request.user.role == 'admin'
            or self.request.user.is_superuser
        )

    def handle_no_permission(self):
        from django.contrib import messages
        messages.error(self.request, "You can only delete categories you created.")
        return HttpResponseRedirect(reverse('writesphere:home'))

    def get(self, request, *args, **kwargs):
        # Directly delete on GET without a confirmation template
        return self.post(request, *args, **kwargs)

