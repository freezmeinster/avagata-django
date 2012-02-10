# Create your views here.
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from event.models import Event

def index(request):
    list_event = Event.objects.filter(status=True)
    return render_to_response('event/home.html',{
      'events': list_event,
      }, context_instance=RequestContext(request))

def detail(request, event_id):
    event = Event.objects.get(id=event_id)
    return render_to_response("event/detail.html",{
      'event' : event,
      }, context_instance=RequestContext(request))