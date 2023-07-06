from django.urls import path
from .views import chatroom, room

urlpatterns = [
    path("", chatroom, name="home"),
    path("<str:room_name>/", room, name="room"),
]