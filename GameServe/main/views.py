# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello, world. You're at the poll index.")

# from django.http import HttpResponse
# from django.template import RequestContext, loader

# from polls.models import Poll

# def index(request):
#     latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = RequestContext(request, {
#         'latest_poll_list': latest_poll_list,
#     })
#     return HttpResponse(template.render(context))

from django.shortcuts import render

# from main.models import Main

def index(request):
    # latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render(request, 'main/index.html')

def browse(request):
    # latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render(request, 'main/browse.html')

def user(request):
    # latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render(request, 'main/user.html')

def game(request):
    # latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render(request, 'main/game.html')

def create(request):
    # latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render(request, 'main/create.html')


# from django.shortcuts import render_to_response   # <- Does django.http.HttpResponse + django.shortcuts.render in one command
# from django.template import RequestContext
# # from mainApp.models import Sport, Court

# # A view ALWAYS takes a request as a argument
# def index(request):
#     context = RequestContext(request)
#     # context_dict = {'sports': Sport.objects.order_by('sportType'), 'courts': Court.objects.order_by('longitude')}
#     return render_to_response('main/index.html', context)
