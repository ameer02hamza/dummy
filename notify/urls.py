import django_eventstream
from django.contrib import admin
from django.urls import path, include
from .views import home, notifications

urlpatterns = [
    path('', home),
    path('noti/<room_id>', home),
    path('noti/<room_id>/messages', notifications),
    path('noti/<room_id>/events/', include(django_eventstream.urls), {
        'format-channels': ['room-{room_id}']
    }),
]
