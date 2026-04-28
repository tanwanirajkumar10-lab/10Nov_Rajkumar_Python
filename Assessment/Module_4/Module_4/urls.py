from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('writesphere.urls')),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    
    # Error Page Previews (Only for development)
    path('404/', TemplateView.as_view(template_name='404.html')),
    path('500/', TemplateView.as_view(template_name='500.html')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
