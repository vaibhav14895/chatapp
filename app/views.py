from django.shortcuts import render
from .models import chatroom,Chats
def chathome(request):
    chatrooms =chatroom.objects.all()
    return render(request,'chatapp/chatappindex.html',{'chatrooms':chatrooms})


def individualchat(request,slug):
    chatrooms=chatroom.objects.get(slug=slug)
    chatmessages=Chats.objects.filter(room= chatrooms)[0:30]
    return render(request,'chatapp/room.html',{'chatrooms':chatrooms,'chatmessages':chatmessages})