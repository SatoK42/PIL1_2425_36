import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Récupère le nom du salon depuis l'URL
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        # Crée un nom de groupe unique pour ce salon
        self.room_group_name = f'chat_{self.room_name}'

        # Ajoute ce consommateur (cette connexion) au groupe
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()  # Accepte la connexion WebSocket

    async def disconnect(self, close_code):
        # Retire la connexion du groupe à la déconnexion
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Reçoit un message envoyé par le client
        data = json.loads(text_data)
        message = data['message']
        author = self.scope['user'].username  # Nom de l'utilisateur connecté

        # Envoie ce message à tous les membres du groupe
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'author': author,
            }
        )

    async def chat_message(self, event):
        # Quand un message arrive du groupe, on le renvoie au client
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'author': event['author'],
        }))