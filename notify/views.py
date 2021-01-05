from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
from django_eventstream import get_current_event_id, send_event

#
# def home(request, room_id):
#     print(room_id, request.user.id)
#     if int(room_id) == int(request.user.id):
#         print(room_id, "Room")
#         last_id = get_current_event_id(['room-{}'.format(request.user.id)])
#         print(last_id, "last_id")
#         context = {}
#         context['room_id'] = "room-{}".format(room_id)
#         context['last_id'] = last_id
#         context['messages'] = "hello"
#         context['user'] = request.user.username
#         print(context)
#         print(room_id, 'room-{}'.format(room_id))
#         send_event(last_id, 'message',"hrllo")
#         return render(request, 'user_room.html', context)
#     else:
#         return HttpResponse("You have no room")

def home(request):
    if request.user.is_authenticated:
        print(request.user)

        context = {}
        context['url'] = '/events/'
        context['last_id'] = get_current_event_id(['time'])
        send_event('time', 'message', "helssfdsdlodsd")

        return render(request, 'user_room.html', context)
    else:
        return JsonResponse({"fail":"You are not authenticated"})


def notifications(request, room_id):
    print(room_id)
    print("hello")
    body = {"TEXT":"hello"}
    return HttpResponse(body, content_type='application/json')
