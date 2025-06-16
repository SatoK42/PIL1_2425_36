from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('acceuil/', views.acceuil, name='acceuil'),
    path('logout/', views.logout, name='logout'),
]
