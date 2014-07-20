import json
from django.http import HttpResponse
from django.shortcuts import render
from events.models import *
from django.forms.models import *
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, render
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
#
def index(request):
	context_dict = {
		'upcoming':Event.objects.filter(dateTime__gte=timezone.now()),
	}
	return render_to_response('events/index.html',context_dict, RequestContext(request) )
 
def browse(request):
    return render(request, 'events/browse.html')
 
def user(request):
    return render(request, 'events/user.html')
 
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