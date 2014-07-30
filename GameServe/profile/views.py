from django.shortcuts import render_to_response   # <- Does django.http.HttpResponse + django.shortcuts.render in one command
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from profile.forms import UserForm
from profile.models import User
import json



def ajax(request):
    # Get the tnl info

    print 'ajax'
    if request.method == 'POST':
        if 'username' in request.POST:
            username = request.POST['username']
            password = request.POST['password']

            if len(username) == 0:
                return HttpResponse(json.dumps({'message':'Need to type a username'}), mimetype='application/json')
            if '@' not in username:
                try:
                    chk = User.objects.get(username=username)
                    username = authenticate(email=chk.email, password=password)
                except:
                    pass
            user = authenticate(email=username, password=password)

            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponse(json.dumps({'message':'You are logged in'}), mimetype='application/json', status=200)
                else:
                    return HttpResponse(json.dumps({'message':'Disabled acct'}), mimetype='application/json', status=400)

    else:
        return HttpResponse(json.dumps({'message':'Need POST request idiot'}), mimetype='application/json', status=400)    


def user(request):
    return render_to_response('profile/user.html',{}, RequestContext(request))

# TODO: Do something else here or get rid of it
def index(request):
  context = RequestContext(request)
  context_dict = {}
  return render_to_response('profile/index.html', context_dict, context)

