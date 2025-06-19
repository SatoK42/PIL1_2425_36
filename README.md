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
- MySQL 
- pip

### 1. Cloner le dépôt

```bash
git clone https://github.com/SatoK42/PIL1_2425_36.git
cd PIL1_2425_36
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 3. Configuration de la base de données

- Installez [WampServer](https://sourceforge.net/projects/wampserver/) sur votre machine (en suivant les instructions du site officiel).
- Lancez WampServer puis ouvrez phpMyAdmin (généralement accessible via http://localhost/phpmyadmin).
- Créez une nouvelle base de données:django .
- Notez le nom de la base, l'utilisateur et le mot de passe que vous utiliserez dans le fichier `.env`.
- Une fois la base créée, poursuivez avec les étapes suivantes :

```bash
python manage.py migrate
```

- Enfin, lancez Daphne pour démarrer le serveur ASGI :

```bash
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

> Attention :
> Si vous obtenez une erreur du type
> django.db.utils.OperationalError: (1045, "Access denied for user 'root'@'localhost' (using password: NO)"),
> cela signifie que Django n'arrive pas à se connecter à la base de données MySQL, généralement parce que le nom d'utilisateur, le mot de passe ou les paramètres de connexion sont incorrects ou manquants dans votre configuration.
>Vérifiez que les variables d'environnement DB_USER et DB_PASSWORD sont bien définies dans votre fichier .env et correspondent à un utilisateur MySQL valide.

## Configuration du fichier .env


Exemple de contenu du fichier `.env` :

```
SECRET_KEY=ta_cle_secrete_django
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1,ton_domaine.com
DB_NAME=nom_de_ta_base
DB_USER=utilisateur_mysql
DB_PASSWORD=mot_de_passe_mysql
DB_HOST=localhost
DB_PORT=3306
EMAIL_HOST_USER=ton_email@example.com
EMAIL_HOST_PASSWORD=mot_de_passe_email
```

**N'oublie pas d'adapter ces valeurs à ta configuration !**


## Auteurs

- Groupe PIL1_2425_36 ,IFRI, Université d'Abomey-Calavi