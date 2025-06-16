from django.urls import path
from . import views

app_name = 'profileUser'
urlpatterns = [
    path('', views.profile_view, name='profile'),
    path('edit/', views.profile_edit, name='profile_edit'),
    path('update_vehicle/', views.profile_update_vehicle, name='profile_update_vehicle'),
]