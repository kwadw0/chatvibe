from django.urls import path
from .views import chatroom

urlpatterns = [
    path("", chatroom, name="home"),
]