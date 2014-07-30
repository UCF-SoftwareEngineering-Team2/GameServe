import json
import time
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render
from events.models import *
from django.core import serializers
from django.forms.models import *
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.template import RequestContext
from events.models import Event, RecentActivity, Sport, Court
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
        'events':Event.objects.filter(dateTime__gte=timezone.now())[:10],
        'recent_activity': RecentActivity.objects.all().order_by('-id'),
    }
    return render_to_response('events/index.html',context_dict, RequestContext(request) )

# Returns a set of events as a JSON payload based on a parameter
# i.e. /events/upcoming_events/?numEvents=3 will return the next 3 events occuring next
# A third parameter ('html'), allows an HTML segment to be returned for infinite scrolling
@csrf_exempt
def upcoming_events(request):
    # This gets the first x amount of events after now, x being based on the the url parameter 'numEvents'
    context_dict = {
        'events':Event.objects.filter(dateTime__gte=timezone.now())[:request.GET.get('numEvents')],
    }

    # If the request contains sports, then return an HTML segment because it is looking for filtered data
    if(request.GET.getlist('sports')):
        sports = Sport.objects.filter(sportType__in=request.GET.getlist('sports'))
        courts = Court.objects.filter(sport__in=sports)
        events = Event.objects.filter(court__in=courts, dateTime__gte=timezone.now())[:request.GET.get('numEvents')]
        return render_to_response('events/events_segment.html', {'events':events}, RequestContext(request))


    # Returns either a JSON payload or an HTML segment based on the request
    if(request.GET.get('html')):
        return render_to_response('events/events_segment.html', context_dict, RequestContext(request))
    else:

        # Creates a dictionary based on this, and then returns it as a JSON payload
        jsonPayload = {}
        for index, event in enumerate(context_dict['events']):
            jsonPayload[index] = model_to_dict(event)

            # Also returns a dateTimeStmp parameter as a timestamp in the form of a UTC timestamp
            jsonPayload[index]['dateTimeStamp'] = int(time.mktime(jsonPayload[index]['dateTime'].timetuple()))
            jsonPayload[index]['dateTime'] = unicode(jsonPayload[index]['dateTime'])
            jsonPayload[index]['endTime'] = unicode(jsonPayload[index]['endTime'])
        return HttpResponse(json.dumps(jsonPayload), content_type="application/json")



# Returns a set of events as a JSON payload based on 2 parameters
# i.e. /events/upcoming_events/?numEvents=3&dateTime=1407573840 will return the next 3 events occuring after the datetime 1407573840
# A third parameter ('html'), allows an HTML segment to be returned for infinite scrolling
@csrf_exempt
def upcoming_events_after(request):
    # This gets the first x amount of events after now, x being based on the the url parameter 'numEvents'
    # Also allows for a 'dateTime' parameter in the form of a UTC timestamp so that you can get events only after a certain time
    context_dict = {
        'events':Event.objects.filter(dateTime__gt=datetime.fromtimestamp(float(request.GET.get('dateTime'))))[:request.GET.get('numEvents')],
    }

    # If the request contains sports, then return an HTML segment because it is looking for filtered data
    if(request.GET.getlist('sports')):
        sports = Sport.objects.filter(sportType__in=request.GET.getlist('sports'))
        courts = Court.objects.filter(sport__in=sports)
        events = Event.objects.filter(court__in=courts, dateTime__gt=datetime.fromtimestamp(float(request.GET.get('dateTime'))))[:request.GET.get('numEvents')]
        return render_to_response('events/events_segment.html', {'events':events}, RequestContext(request))

    # Returns either a JSON payload or an HTML segment based on the request
    if(request.GET.get('html')):
        return render_to_response('events/events_segment.html', context_dict, RequestContext(request))
    else:
        # Creates a dictionary based on this, and then returns it as a JSON payload
        jsonPayload = {}
        for index, event in enumerate(context_dict['events']):

            # Also returns a dateTimeStmp parameter as a timestamp in the form of a UTC timestamp
            jsonPayload[index] = model_to_dict(event)
            jsonPayload[index]['dateTime'] = unicode(jsonPayload[index]['dateTime'])
            jsonPayload[index]['endTime'] = unicode(jsonPayload[index]['endTime'])
        return HttpResponse(json.dumps(jsonPayload), content_type="applciation/json")



def browse(request):
    # This returns the first 10 events after the current time
    context_dict = {'events':Event.objects.filter(dateTime__gte=timezone.now())[:15]} 
    context_dict['lastTime'] = int(time.mktime(context_dict['events'].reverse()[0].dateTime.timetuple()))
    return render_to_response('events/browse.html',context_dict, context_instance=RequestContext(request) )
 
def user(request):
    return render(request, 'events/user.html')

def create_account(request):
    return render(request, 'events/create_account.html')
 
def game(request, gameId="1"):
    context_dict = {'event':Event.objects.get(id=int(gameId)),}
    # latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render_to_response('events/game.html',context_dict, RequestContext(request) )
 
def create(request):
    # latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render(request, 'events/create.html')
 
@csrf_exempt
def new_game(request):
    if request.user.is_authenticated():
        creator = request.user.id
    else:
        request.POST['creator']
    #print create event with post data
    newGame = Event.objects.create_event(dateTime = request.POST['dateTime'],
                                         creator = request.POST['creator'], 
                                         court = request.POST['court'],
                                         duration = request.POST['duration'])
    #Create response to POST
    response = {}
 
    #If new game is a string, it's an error
    if(type(newGame) is str):
        response['result'] = newGame
    #Otherwise it's an instance of a game, so send a JSON payload back with event information (CURRENTLY FOR DEBUGGING PURPOSES)
    else:
        RecentActivity.objects.add_activity(activity="Created game", event=newGame)
        response['result'] = model_to_dict(newGame)
        response['result']['dateTime'] = str(response['result']['dateTime'])
        response['result']['endTime'] = str(response['result']['endTime'])
    return HttpResponse(json.dumps(response), content_type="applciation/json") 
 
@csrf_exempt
def commit(request):
    if request.method == 'GET':
        return HttpResponseRedirect('/events/create/')

    newGame = Event.objects.add_participant(user=request.user.id, event=request.POST['event'])
    #Create response to POST
    response = {}
    #If new game is a string, it's an error
    if(type(newGame) is str):
        response['result'] = newGame
    #Otherwise it's an instance of a game, so send a JSON payload back with event information (CURRENTLY FOR DEBUGGING PURPOSES)
    else:
        RecentActivity.objects.add_activity(activity="Committed", event=newGame)
        response['result'] = model_to_dict(newGame)
        response['result']['dateTime'] = str(response['result']['dateTime'])
        response['result']['endTime'] = str(response['result']['endTime'])
    return HttpResponse(json.dumps(response), content_type="application/json")
 
@csrf_exempt
def uncommit(request):
    newGame = Event.objects.remove_participant(user=request.user.id, event=request.POST['event'])
    #Create response to POST
    response = {}
    #If new game is a string, it's an error
    if(type(newGame) is str):
        response['result'] = newGame
    #Otherwise it's an instance of a game, so send a JSON payload back with event information (CURRENTLY FOR DEBUGGING PURPOSES)
    else:
        RecentActivity.objects.add_activity(activity="Uncommitted", event=newGame)
        response['result'] = model_to_dict(newGame)
        response['result']['dateTime'] = str(response['result']['dateTime'])
        response['result']['endTime'] = str(response['result']['endTime'])
    return HttpResponse(json.dumps(response), content_type="applciation/json")


#function for testing the results of querying for recent activity
@csrf_exempt
def recent_activity(request):
    activity = RecentActivity.objects.get(id=request.POST['id'])
    dict = { 'results' : model_to_dict(activity), }
    return HttpResponse(json.dumps(dict), content_type="application/json")
