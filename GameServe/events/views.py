import json
import time
from django.http import HttpResponse
from django.shortcuts import render
from events.models import *
from django.forms.models import *
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.template import RequestContext
from events.models import Event
from tastypie.utils import timezone
 
# 
# This section sets up the ability to log to console for debugging.
# logging
# 
import logging, logging.config, sys
LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
        }
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO'
    }
}
logging.config.dictConfig(LOGGING)
#
# ./logging
#
# NOTE: @csrf_exempt decorator is temporary to allow for testing with a REST client
#

@csrf_exempt
def index(request):
    # This returns the first 10 events after the current time
    context_dict = {
        'upcoming':Event.objects.filter(dateTime__gte=timezone.now())[:10],
    }
    return render_to_response('events/index.html',context_dict, RequestContext(request) )

# Returns a set of events as a JSON payload based on a parameter
# i.e. /events/upcoming_events/?numEvents=3 will return the next 3 events occuring next
@csrf_exempt
def upcoming_events(request):
    # This gets the first x amount of events after now, x being based on the the url parameter 'numEvents'
    context_dict = {
        'upcoming':Event.objects.filter(dateTime__gte=timezone.now())[:request.GET.get('numEvents')],
    }

    # Creates a dictionary based on this, and then returns it as a JSON payload
    testing = {}
    for index, event in enumerate(context_dict['upcoming']):
        testing[index] = model_to_dict(event)

        # Also returns a dateTimeStmp parameter as a timestamp in the form of a UTC timestamp
        testing[index]['dateTimeStamp'] = int(time.mktime(testing[index]['dateTime'].timetuple()))
        testing[index]['dateTime'] = unicode(testing[index]['dateTime'])
        testing[index]['endTime'] = unicode(testing[index]['endTime'])
    return HttpResponse(json.dumps(testing), content_type="applciation/json")

# Returns a set of events as a JSON payload based on 2 parameters
# i.e. /events/upcoming_events/?numEvents=3&dateTime=1407573840 will return the next 3 events occuring after the datetime 1407573840
@csrf_exempt
def upcoming_events_after(request):
    # This gets the first x amount of events after now, x being based on the the url parameter 'numEvents'
    # Also allows for a 'dateTime' parameter in the form of a UTC timestamp so that you can get events only after a certain time
    context_dict = {
        'upcoming':Event.objects.filter(dateTime__gt=datetime.fromtimestamp(float(request.GET.get('dateTime'))))[:request.GET.get('numEvents')],
    }

    # Creates a dictionary based on this, and then returns it as a JSON payload
    testing = {}
    for index, event in enumerate(context_dict['upcoming']):

        # Also returns a dateTimeStmp parameter as a timestamp in the form of a UTC timestamp
        testing[index] = model_to_dict(event)
        testing[index]['dateTime'] = unicode(testing[index]['dateTime'])
        testing[index]['endTime'] = unicode(testing[index]['endTime'])
    return HttpResponse(json.dumps(testing), content_type="applciation/json")


def browse(request):
    return render(request, 'events/browse.html')
 
def user(request):
    return render(request, 'events/user.html')

def create_account(request):
    return render(request, 'events/create_account.html')
 
def game(request):
    context_dict = {
        'event':Event.objects.get(id=111),
    }
    # latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render_to_response('events/game.html',context_dict, RequestContext(request) )
 
def create(request):
    # latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render(request, 'events/create.html')
 
@csrf_exempt
def new_game(request):
    #print create event with post data
    newGame = Event.objects.create_event(dateTime = request.POST['dateTime'],creator = request.POST['creator'],court = request.POST['court'],duration = request.POST['duration'])
    #Create response to POST
    response = {}
 
    #If new game is a string, it's an error
    if(type(newGame) is str):
        response['result'] = newGame
    #Otherwise it's an instance of a game, so send a JSON payload back with event information (CURRENTLY FOR DEBUGGING PURPOSES)
    else:
        response['result'] = model_to_dict(newGame)
        response['result']['dateTime'] = str(response['result']['dateTime'])
        response['result']['endTime'] = str(response['result']['endTime'])
    return HttpResponse(json.dumps(response), content_type="applciation/json") 
 
@csrf_exempt
def commit(request):
    #
    # NOTE / TODO: current input (user=1) is PLACEHOLDER
    #
    newGame = Event.objects.add_participant(user=1, event=request.POST['event'])
    #Create response to POST
    response = {}
    #If new game is a string, it's an error
    if(type(newGame) is str):
        response['result'] = newGame
    #Otherwise it's an instance of a game, so send a JSON payload back with event information (CURRENTLY FOR DEBUGGING PURPOSES)
    else:
        response['result'] = model_to_dict(newGame)
        response['result']['dateTime'] = str(response['result']['dateTime'])
        response['result']['endTime'] = str(response['result']['endTime'])
    return HttpResponse(json.dumps(response), content_type="applciation/json")
 
@csrf_exempt
def uncommit(request):
    #
    # NOTE / TODO: current input (user=1) is PLACEHOLDER
    #
    newGame = Event.objects.remove_participant(user=1, event=request.POST['event'])
    #Create response to POST
    response = {}
    #If new game is a string, it's an error
    if(type(newGame) is str):
        response['result'] = newGame
    #Otherwise it's an instance of a game, so send a JSON payload back with event information (CURRENTLY FOR DEBUGGING PURPOSES)
    else:
        response['result'] = model_to_dict(newGame)
        response['result']['dateTime'] = str(response['result']['dateTime'])
        response['result']['endTime'] = str(response['result']['endTime'])
    return HttpResponse(json.dumps(response), content_type="applciation/json")
