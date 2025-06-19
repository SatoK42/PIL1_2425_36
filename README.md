# IFRI Comotorage

Plateforme de covoiturage universitaire avec messagerie en temps réel, gestion de profils et notifications.

## Fonctionnalités principales

- Authentification : Inscription, connexion, gestion des mots de passe.
- Messagerie : Chat en temps réel entre utilisateurs (WebSocket via Django Channels).
- Gestion de profils : Modification et affichage du profil utilisateur.
- Trajets : Création, recherche et gestion de trajets de covoiturage.
- Notifications : Système de notifications pour les nouveaux messages ou trajets.

## Installation

### Prérequis

- Python 3.11 ou supérieur
- MySQL (ou autre SGBD compatible)
- pip

### 1. Cloner le dépôt

Placez-vous dans le dossier du projet.

### 2. Installer les dépendances

```
pip install -r requirements.txt
```

### 3. Configuration de la base de données

- Créez une base de données MySQL.
- Configurez les paramètres dans `IFRI_comotorage/IFRI_comotorage/settings.py` (section `DATABASES`).

### 4. Appliquer les migrations

```
python manage.py migrate
```

### 5. Créer un superutilisateur

```
python manage.py createsuperuser
```

### 6. Lancer le serveur en mode développement

```
python manage.py runserver
```

### 7. Lancer le serveur ASGI (pour WebSocket/Channels)

```
cd IFRI_comotorage
python -m daphne -b 0.0.0.0 -p 8000 IFRI_comotorage.asgi:application
```

## Structure du projet

- auth_app/ : Gestion de l'authentification et des utilisateurs
- messaging_app/ : Messagerie temps réel (WebSocket)
- profileUser/ : Gestion des profils utilisateurs
- trajet/ : Gestion des trajets de covoiturage
- static/ : Fichiers statiques (CSS, JS, images)
- media/ : Fichiers uploadés par les utilisateurs

## Utilisation

- Accès à l'interface web : http://localhost:8000/ (s'assurer que le port 8000 est libre sinon utiliser un autre port ex: 8001)
- Accès à l'admin : http://localhost:8000/admin/

## Dépendances principales

- Django
- Channels
- Daphne
- channels_redis
- mysqlclient
- pillow

## Notes

- Pour le développement sous Windows, si `mysqlclient` pose problème, voir les instructions dans `requirements.txt` pour utiliser PyMySQL.
- Pour la messagerie en temps réel, assurez-vous que Redis est installé et configuré si vous utilisez `channels_redis`.

## Auteurs

- Groupe PIL1_2425_36 ,IFRI, Université d'Abomey-Calavi