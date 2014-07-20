import json
from django.http import HttpResponse
from django.shortcuts import render
from events.models import *
from django.forms.models import *
from django.views.decorators.csrf import csrf_exempt

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

def index(request):
    return render(request, 'events/index.html')

def browse(request):
    return render(request, 'events/browse.html')

def user(request):
    return render(request, 'events/user.html')

def game(request):
    return render(request, 'events/game.html')

def create(request):
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