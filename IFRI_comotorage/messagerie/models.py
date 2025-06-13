from django.db import models
from django.conf import settings


class Conversation(models.Model):
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='conversations', through='ConversationUser')
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation {self.id}"

class ConversationUser(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='conversation_users')

    def __str__(self):
        return f"{self.user.username} in conv {self.conversation.id}"

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='messages', on_delete=models.CASCADE)
    contenu = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Msg de {self.auteur.username} ({self.timestamp})"
