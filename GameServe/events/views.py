from django.shortcuts import render_to_response
from django.template import RequestContext


# from events.serializers import CourtSerializer, EventSerializer
from events.models import Court, Event, Sport



def index(request):
    context_dict = {'courts':Court.objects.all()}
    return render_to_response('events/index.html',context_dict, RequestContext(request))
