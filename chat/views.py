from django.shortcuts import render
from django.utils.safestring import mark_safe
from .models import Message
import json

def index(request):
    return render(request, 'chat/index.html', {})


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })

def log_create(request):
    if request.method == 'POST':
        message = Message()
        message.text = request.POST['message_text']
        message.save()
    else:
        return render(request, 'chat/log.html', {})