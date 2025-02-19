from django.shortcuts import render
from django.http import HttpResponse  # Import HttpResponse
from .models import Message

def chat_view(request):
    messages = Message.objects.all()
    return render(request, 'chat/chat.html', {'messages': messages})

def ts_view(request):  # This function handles requests to /chat/ts/
    return render(request, 'chat/ts.html')

