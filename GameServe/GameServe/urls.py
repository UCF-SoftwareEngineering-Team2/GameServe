from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'GameServe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', TemplateView.as_view( template_name='homepage.html'), name='home'),
    url(r'^accounts/', include('accounts.urls'), name='accounts'),
    url(r'^auth/', 'django.contrib.auth.views.login'),
    url(r'^admin/', include(admin.site.urls)),
)