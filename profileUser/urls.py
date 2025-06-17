from django.urls import path
from . import views

app_name = 'profileUser'
urlpatterns = [
    path('', views.profile_view, name='profile'),
    path('edit/', views.profile_edit, name='profile_edit'),
]