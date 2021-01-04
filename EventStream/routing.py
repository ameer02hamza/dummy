from channels.routing import ProtocolTypeRouter, URLRouter
import notify.routing

application = ProtocolTypeRouter({
    'http': URLRouter(notify.routing.urlpatterns),
})

