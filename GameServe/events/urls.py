from django.conf.urls import patterns, url

from events import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^browse/', views.browse, name='browse'),
    url(r'^create/', views.create, name='create'),
    url(r'^game/', views.game, name='game'),
    url(r'^user/', views.user, name='user')
)