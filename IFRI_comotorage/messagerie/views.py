from django.shortcuts import render, get_object_or_404
from .models import Conversation

# Affiche la liste des salons de chat
def chat_list(request):
    convs = Conversation.objects.filter(participants=request.user)
    return render(request, 'messagerie/chat_list.html', {'convs': convs})

# Affiche une salle de chat précise
def chat_room(request, room_name):
    conv = get_object_or_404(Conversation, id=room_name)
    return render(request, 'messagerie/chat_room.html', {
        'conv': conv,
        'room_name': room_name,
    })
