 
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('event.views',
    url(r'^$','index',name='event_index'),
    url(r'^detail/(?P<event_id>\d+)', 'detail', name='event_detail'),
    )
