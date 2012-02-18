from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('landing.views',
    url(r'^$','index',name='landing_index'),
    url(r'^static/', 'static', name='landing_static'),
    url(r'^feature/(?P<feature_id>\d+)','read_feature',name='landing_read_feature'),
    )
