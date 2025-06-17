from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('acceuil/', views.acceuil, name='acceuil'),
    path('logout/', views.logout, name='logout'),
    path('reinitialiser/', views.verification_utilisateur, name='reinitialiser'),
    path('changer-mot-de-passe/<int:utilisateur_id>/', views.changer_mdp, name='changer_mdp'),
]
