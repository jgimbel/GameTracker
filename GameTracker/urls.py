from django.conf.urls import patterns, include, url
from django.contrib import admin
from game_tracker import Controllers
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'GameTracker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^/?$', Controllers.Index.index)
)
