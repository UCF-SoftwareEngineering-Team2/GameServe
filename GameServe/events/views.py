from django.shortcuts import render

# from main.models import Main

def index(request):
    return render(request, 'events/index.html')

def browse(request):
    # latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render(request, 'events/browse.html')

def user(request):
    # latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render(request, 'events/user.html')

def game(request):
    # latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render(request, 'events/game.html')

def create(request):
    # latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render(request, 'events/create.html')
