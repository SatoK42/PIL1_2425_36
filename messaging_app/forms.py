from django import forms
from django.contrib.auth import get_user_model
from .models import Conversation, Message
User = get_user_model()

class NewConversationForm(forms.ModelForm):
    class Meta:
        model = Conversation
        fields = ['is_group', 'name']  # les deux champs de ton modèle
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du groupe…'}),
            'is_group': forms.CheckboxInput(),
        }

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text', 'image', 'audio']
        widgets = {
            'text': forms.Textarea(attrs={'class':'form-control','rows':2,'placeholder':'Écrire un message...'}),
        }