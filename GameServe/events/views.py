from django.shortcuts import render_to_response, render
from django.template import RequestContext
from events.models import Event
from tastypie.utils import timezone
 
def index(request):
	context_dict = {
		'upcoming':Event.objects.filter(dateTime__gte=timezone.now()),
	}
	return render_to_response('events/index.html',context_dict, RequestContext(request) )
 
def browse(request):
    # latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render(request, 'events/browse.html')
 
def user(request):
    # latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
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