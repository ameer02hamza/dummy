from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
from django_eventstream import get_current_event_id, send_event


def home(request, room_id=None):
    print(room_id, request.user.id)
    if int(room_id) == request.user.id:
        print(room_id)
        last_id = get_current_event_id(['room-{}'.format(request.user.id)])
        print(last_id)
        context = {}
        context['room_id'] = "room-{}".format(room_id)
        context['last_id'] = last_id
        context['messages'] = "hello"
        context['user'] = request.user.username
        print(context)
        print(room_id, 'room-{}'.format(room_id))
        send_event('room-{}'.format(room_id), 'message', {'text': 'hello world'})
        return render(request, 'user_room.html', context)
    else:
        return HttpResponse("You have no room")


def notifications(request, room_id):
    print(room_id)
    print("hello")
    return JsonResponse({"Hello": "Hello world", "h": "jdk"})
