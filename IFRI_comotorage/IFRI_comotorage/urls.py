from django.contrib import admin
from django.urls import path, include
from auth_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('acceuil/', views.acceuil, name='acceuil'),
    path('edit/', views.edit, name='edit'),
    path('chat/', include('messagerie.urls')),
]
