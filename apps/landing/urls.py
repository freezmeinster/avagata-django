from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('landing.views',
    url(r'^$','index',name='landing_index'),
    url(r'^static/', 'static', name='landing_static'),
    )
