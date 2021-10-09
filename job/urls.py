from projects.views import projects
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('devjobs/', admin.site.urls),
    path('projects/', include('projects.urls')),
    path('', include('users.urls')),
] + static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += static (settings.STATIC_URL, document_root = settings.STATIC_ROOT) 