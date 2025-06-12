from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.chat_list, name='chat_list'),
    path('room/<int:room_name>/', views.chat_room, name='chat_room'),
]