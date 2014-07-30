from django.conf.urls import patterns, url

from events import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^browse/', views.browse, name='browse'),
    url(r'^create/', views.create, name='create'),
    
    # Gets game by a specific gameId
    url(r'^game/(?P<gameId>\w+)/', views.game, name='game'),
    url(r'^new_game/', views.new_game, name='new_game'),
    url(r'^commit/', views.commit, name='commit'),
    url(r'^uncommit/', views.uncommit, name='uncommit'),
    url(r'^upcoming_events/', views.upcoming_events, name='upcoming_events'),
    url(r'^upcoming_events_after/', views.upcoming_events_after, name='upcoming_events_after'),
)