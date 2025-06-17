from django.conf import settings
from django.db import models


class Conversation(models.Model):
    """
    Une conversation peut être privée ou un groupe.
    """
    is_group = models.BooleanField(default=False)
    name = models.CharField(max_length=255, blank=True, null=True)
    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='conversations'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def latest_message(self):
        return self.messages.order_by('-timestamp').first()

    def __str__(self):
        if self.is_group:
            return self.name or f"Groupe {self.id}"
        return f"Conversation privée #{self.id}"


class Message(models.Model):
    """
    Message dans une conversation.
    """
    is_read = models.BooleanField(default=False)
    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name='messages'
    )
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='sent_messages'
    )
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='chat/images/', blank=True, null=True)
    audio = models.FileField(upload_to='chat/audios/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"{self.sender}: {self.text or '[media]'}"
