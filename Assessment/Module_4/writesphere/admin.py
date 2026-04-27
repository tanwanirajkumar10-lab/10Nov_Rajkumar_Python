from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import User, Category, Tag, Post, Comment, Like, Follow

# ─── Admin Site Branding ───────────────────────────────────────────────────────
admin.site.site_header  = "WriteSphere Administration"
admin.site.site_title   = "WriteSphere Admin"
admin.site.index_title  = "Welcome to WriteSphere Admin Panel"


# ─── User Admin ────────────────────────────────────────────────────────────────
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Role & WriteSphere Info', {'fields': ('role',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Role', {'fields': ('role',)}),
    )
    list_display  = ('username', 'email', 'first_name', 'last_name', 'role_badge', 'is_staff', 'is_active', 'date_joined')
    list_filter   = ('role', 'is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering      = ('-date_joined',)

    @admin.display(description='Role')
    def role_badge(self, obj):
        colours = {'admin': '#dc3545', 'author': '#0d6efd', 'reader': '#198754'}
        colour  = colours.get(obj.role, '#6c757d')
        return format_html(
            '<span style="background:{};color:#fff;padding:2px 8px;border-radius:4px;font-size:12px">{}</span>',
            colour, obj.role.capitalize()
        )


# ─── Category Admin ────────────────────────────────────────────────────────────
class CategoryAdmin(admin.ModelAdmin):
    list_display        = ('name', 'slug', 'creator', 'post_count')
    search_fields       = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields     = ('creator',)

    @admin.display(description='Posts')
    def post_count(self, obj):
        return obj.posts.count()


# ─── Tag Admin ─────────────────────────────────────────────────────────────────
class TagAdmin(admin.ModelAdmin):
    list_display        = ('name', 'slug', 'post_count')
    search_fields       = ('name',)
    prepopulated_fields = {'slug': ('name',)}

    @admin.display(description='Posts')
    def post_count(self, obj):
        return obj.posts.count()


# ─── Inline Comments inside PostAdmin ─────────────────────────────────────────
class CommentInline(admin.TabularInline):
    model       = Comment
    extra       = 0
    readonly_fields = ('author', 'content', 'created_at')
    can_delete  = True


# ─── Post Admin ────────────────────────────────────────────────────────────────
class PostAdmin(admin.ModelAdmin):
    list_display        = ('title', 'author', 'category_list', 'like_count', 'comment_count', 'created_at')
    list_filter         = ('categories', 'created_at', 'author__role')
    search_fields       = ('title', 'content', 'author__username')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal   = ('categories', 'tags')
    readonly_fields     = ('created_at', 'updated_at', 'cover_preview')
    date_hierarchy      = 'created_at'
    inlines             = [CommentInline]

    fieldsets = (
        ('Content', {
            'fields': ('title', 'slug', 'content', 'cover_image', 'cover_preview')
        }),
        ('Taxonomy', {
            'fields': ('categories', 'tags')
        }),
        ('Meta', {
            'fields': ('author', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    @admin.display(description='Categories')
    def category_list(self, obj):
        return ", ".join([c.name for c in obj.categories.all()]) or "—"

    @admin.display(description='Likes')
    def like_count(self, obj):
        return obj.likes.count()

    @admin.display(description='Comments')
    def comment_count(self, obj):
        return obj.comments.count()

    @admin.display(description='Cover Preview')
    def cover_preview(self, obj):
        if obj.cover_image:
            return format_html('<img src="{}" style="max-height:150px;border-radius:6px;" />', obj.cover_image.url)
        return "No image"


# ─── Comment Admin ─────────────────────────────────────────────────────────────
class CommentAdmin(admin.ModelAdmin):
    list_display    = ('author', 'post', 'short_content', 'created_at')
    list_filter     = ('created_at',)
    search_fields   = ('author__username', 'post__title', 'content')
    readonly_fields = ('author', 'post', 'created_at')

    @admin.display(description='Comment')
    def short_content(self, obj):
        return obj.content[:80] + ('…' if len(obj.content) > 80 else '')


# ─── Like Admin ────────────────────────────────────────────────────────────────
class LikeAdmin(admin.ModelAdmin):
    list_display  = ('user', 'post', 'created_at')
    list_filter   = ('created_at',)
    search_fields = ('user__username', 'post__title')


# ─── Follow Admin ──────────────────────────────────────────────────────────────
class FollowAdmin(admin.ModelAdmin):
    list_display  = ('follower', 'following', 'created_at')
    list_filter   = ('created_at',)
    search_fields = ('follower__username', 'following__username')


# ─── Role-based access: restrict Author/Reader from sensitive models ───────────
class RoleRestrictedMixin:
    """
    Authors can only see & edit their own records.
    Readers have no admin access (blocked at has_module_perms level).
    """
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser or getattr(request.user, 'role', None) == 'admin':
            return qs
        if getattr(request.user, 'role', None) == 'author':
            # Authors only see their own posts
            if hasattr(qs.model, 'author'):
                return qs.filter(author=request.user)
        return qs.none()

    def has_module_perms(self, request, app_label):
        if getattr(request.user, 'role', None) == 'reader':
            return False
        return super().has_module_perms(request, app_label)


# ─── Register all models ───────────────────────────────────────────────────────
admin.site.register(User, CustomUserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Follow, FollowAdmin)
