from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.db.models import Max, Q
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from .forms import NewConversationForm
from .models import Conversation, Message

User = get_user_model()

@login_required
def api_conversations(request):
    qs = (
        Conversation.objects
        .filter(participants=request.user)
        .annotate(last_msg=Max('messages__timestamp'))
        .order_by('-last_msg')
    )
    data = []
    for c in qs:
        other_qs = c.participants.exclude(id=request.user.id)
        data.append({
            'id': c.id,
            'is_group': c.is_group,
            'name': c.name,
            'last_msg': c.last_msg.isoformat() if c.last_msg else None,
            'other_participants': [
                {
                  'id': u.id,
                  'email': u.email,
                  'name': u.get_full_name() or ''
                }
                for u in other_qs
            ]
        })
    return JsonResponse(data, safe=False)


@login_required
def api_messages(request, convo_id):
    convo = get_object_or_404(Conversation, id=convo_id, participants=request.user)
    msgs = Message.objects.filter(conversation=convo).order_by('timestamp')
    data = []
    for m in msgs:
        # Protection contre les messages sans sender
        if m.sender is None:
            continue
        data.append({
          'id': m.id,
          'sender': m.sender.username,
          'sender_display': m.sender.get_full_name() or m.sender.email,
          'text': m.text,
          'timestamp': m.timestamp.isoformat()
        })
    return JsonResponse(data, safe=False)


@login_required
def conversation_main(request, convo_id=None):
    conversations = Conversation.objects.filter(participants=request.user)
    active_conversation = None
    if convo_id:
        active_conversation = get_object_or_404(Conversation, id=convo_id, participants=request.user)

    return render(request, 'messaging_app/conversation_main.html', {
        'conversations': conversations,
        'active_conversation': active_conversation,
        'active_conversation_id': convo_id
    })

@login_required
def conversation_detail(request, convo_id):
    convo = get_object_or_404(Conversation, id=convo_id, participants=request.user)
    messages = Message.objects.filter(conversation=convo).order_by('timestamp')
    return render(request, 'messaging_app/conversation_detail.html', {
        'active_conversation': convo,
        'messages': messages
    })

@login_required
def new_conversation(request):
    if request.method == 'POST':
        form = NewConversationForm(request.POST)
        participants_ids = request.POST.getlist('participants')
        if form.is_valid():
            # Si c'est une conversation privée (non-groupe), vérifier si elle existe déjà
            if not form.cleaned_data['is_group'] and len(participants_ids) == 1:
                # Chercher une conversation privée existante entre les 2 participants
                existing_convo = Conversation.objects.filter(
                    is_group=False,
                    participants=request.user
                ).filter(
                    participants__id=participants_ids[0]
                ).first()
                
                if existing_convo:
                    # Rediriger vers la conversation existante
                    return redirect('messaging:conversation_main', convo_id=existing_convo.id)
            
            # Sinon, créer une nouvelle conversation
            convo = form.save(commit=False)
            convo.created_by = request.user
            convo.save()

            # On ajoute le créateur + tous les participants
            convo.participants.add(request.user, *participants_ids)

            # Enfin on redirige VRAIMENT vers la room
            return redirect('messaging:conversation_main', convo_id=convo.id)
    else:
        form = NewConversationForm()

    return render(request, 'messaging_app/new_conversation.html', {
        'form': form
    })

@login_required
def search_users(request):
    q = request.GET.get('q','').strip()
    if not q:
        return JsonResponse([], safe=False)

    # On cherche dans l'email, le prénom ou le nom
    qs = User.objects.filter(
        Q(email__icontains=q)
        | Q(first_name__icontains=q)
        | Q(last_name__icontains=q)
    )[:10]

    data = [
        {
            'id':    u.id,
            'email': u.email,
            'name':  (u.get_full_name().strip() or u.email)
        }
        for u in qs
    ]
    return JsonResponse(data, safe=False)
