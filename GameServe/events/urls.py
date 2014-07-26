from django.conf.urls import patterns, url

from events import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^browse/', views.browse, name='browse'),
    url(r'^create/', views.create, name='create'),
    url(r'^game/', views.game, name='game'),
    url(r'^user/', views.user, name='user'),
    url(r'^new_game/', views.new_game, name='new_game'),
    url(r'^create_account/', views.create_account, name='create_account'),
    url(r'^commit/', views.commit, name='commit'),
    url(r'^uncommit/', views.uncommit, name='uncommit')
)