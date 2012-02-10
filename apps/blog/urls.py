from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('blog.views',
    url(r'^$','index',name='blog_index'),
    url(r'^read/', 'read', name='blog_read'),
    )
