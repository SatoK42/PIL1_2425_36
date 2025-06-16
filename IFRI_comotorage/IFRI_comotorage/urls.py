from django.contrib import admin
from django.urls import path, include
from auth_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.register, name='register'),
    path('auth/', include('auth_app.urls')),
    path('profile/', include('profileUser.urls')),
    path('acceuil/', views.acceuil, name='acceuil'),
    path('chat/', include('messaging_app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)