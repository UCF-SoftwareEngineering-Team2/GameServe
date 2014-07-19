from django.conf.urls import patterns, include, url
# from django.views.generic import TemplateView
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
    # url(r'^$', TemplateView.as_view( template_name='homepage.html'), name='home'),
    url(r'^$', include('events.urls'), name='events'),
    url(r'^api/', include(v1_api.urls)),

    (r'^accounts/logout/$', 'django.contrib.auth.views.logout',{'next_page': '/'}),
    url(r'^accounts/', include('allauth.urls')),
    
    url(r'^profile/', include('profile.urls'), name='profile'),
    url(r'^events/', include('events.urls'), name='events'),
    url(r'^admin/', include(admin.site.urls)),
)
