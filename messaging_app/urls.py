from django.urls import path
from . import views

app_name = 'messaging'

urlpatterns = [
    path('', views.conversation_list, name='list'),
    path('new/', views.new_conversation, name='new_conversation'),
    path('chat/<int:convo_id>/', views.conversation_detail, name='conversation_detail'),
    path('search-users/', views.search_users, name='search_users'),
    path('api/conversations/', views.api_conversations, name='api_conversations'),
    path('api/conversations/<int:convo_id>/messages/', views.api_messages, name='api_messages'),
    path('chat/search_users/', views.search_users, name='search_users'),
]
# This file defines the URL patterns for the messaging application, allowing users to view conversations,
# start new conversations, view conversation details, and search for users to add to conversations.