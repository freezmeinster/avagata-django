from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blog.views.index', name='home'),
    (r'^asset/(?P<path>.*)$', 'django.views.static.serve',
	{'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
    url(r'^admin/', include(admin.site.urls)),
)
