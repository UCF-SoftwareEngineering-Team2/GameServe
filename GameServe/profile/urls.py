from django.conf.urls import patterns, url
from profile import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'GameServe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^ajax/$', views.ajax, name='ajax'),
    url(r'^user/$', views.user, name='user')
)
