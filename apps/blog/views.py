# Create your views here.
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from blog.models import Post,Kategori
from landing.models import LandingConfig

def index(request):
    list_post = Post.objects.filter(status=True)
    return render_to_response('blog/home.html',{
        'posting' : list_post, 
        },context_instance=RequestContext(request))
    
def read(request):
    pass
