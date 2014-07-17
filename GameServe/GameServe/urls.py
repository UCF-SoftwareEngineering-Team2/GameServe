from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from tastypie.api import Api
from events.api import *
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(EventResource())
v1_api.register(CourtResource())
v1_api.register(SportResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'GameServe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', TemplateView.as_view( template_name='homepage.html'), name='home'),
    url(r'^accounts/', include('accounts.urls'), name='accounts'),
    url(r'^events/', include('events.urls'), name='events'),
    (r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
)