from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('doc.views',
    url(r'^$','index',name='doc_index'),
    )
