import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
from asgiref.sync import sync_to_async
from .models import Conversation, Message

User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.convo_id = self.scope['url_route']['kwargs']['convo_id']
        self.group_name = f'conversation_{self.convo_id}'

        # Vérifier que l'utilisateur fait partie de la conversation
        user = self.scope['user']
        if not user.is_authenticated:
            await self.close()
            return
        convo = await sync_to_async(Conversation.objects.get)(id=self.convo_id)
        participants = await sync_to_async(lambda: list(convo.participants.values_list('id', flat=True)))()
        if user.id not in participants:
            await self.close()
            return

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        text = data.get('text')
        user = self.scope['user']

        # Créer et sauvegarder le message
        message = await sync_to_async(Message.objects.create)(
            conversation_id=self.convo_id,
            sender=user,
            text=text
        )
        payload = {
            'sender': user.get_full_name(),
            'text': message.text,
            'timestamp': message.timestamp.isoformat()
        }
        # Diffuser au groupe
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'chat_message',
                'message': payload
            }
        )

    async def chat_message(self, event):
        # Envoyer le message JSON au WebSocket
        await self.send(text_data=json.dumps(event['message']))
