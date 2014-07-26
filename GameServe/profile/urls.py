from django.conf.urls import patterns, url
from profile import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'GameServe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'), # ADD NEW PATTERN!
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^ajax/$', views.ajax, name='ajax'),
)
