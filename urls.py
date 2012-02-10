from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'landing.views.home', name='home'),
    url(r'^landing/',  include('landing.urls')),
    url(r'^blog/',  include('blog.urls')),
    
    (r'^asset/(?P<path>.*)$', 'django.views.static.serve',
	{'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
    
    url(r'^admin/', include(admin.site.urls)),
    
)
