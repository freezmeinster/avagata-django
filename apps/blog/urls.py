from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('blog.views',
    url(r'^$','index',name='blog_index'),
    url(r'^read/(?P<post_id>\d+)', 'read', name='blog_read'),
    )
