
from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.chathome),
    path('<slug:slug>/',views.individualchat,name="chatroom"),
]
