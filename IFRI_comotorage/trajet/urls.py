from django.urls import path
from . import views

app_name = 'trajet'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('accepter/<int:trajet_id>/', views.accepter_match, name='accepter_match'),
    path('decliner/<int:trajet_id>/', views.decliner_match, name='decliner_match'),
    path('notifications/', views.notifications_page, name='notifications_page'),
    path('notifications/marquer_lu/<int:notification_id>/', views.marquer_lu, name='marquer_lu'),
]