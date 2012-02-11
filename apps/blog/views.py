from django.core.paginator import Paginator,  EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from blog.models import Post,Kategori
from landing.models import LandingConfig

def index(request):
    posts = Post.objects.filter(status=True)
    paginator = Paginator(posts, 10) 
    page = request.GET.get('page')
    if page == None :
        page = 1
        
    try:
        list_post = paginator.page(page)
    except PageNotAnInteger:
        list_post = paginator.page(1)
    except EmptyPage:
        list_post = paginator.page(paginator.num_pages)    
    
    return render_to_response('blog/home.html',{
        'posting' : list_post, 
        },context_instance=RequestContext(request))
    
def read(request,post_id):
    post = Post.objects.get(id=post_id)
    return render_to_response("blog/read.html",{
        'post' : post,
    },context_instance=RequestContext(request))

def kategori_index(request,kategori_id):
    posts = Post.objects.filter(kategori=kategori_id)
    kat = Kategori.objects.get(id=kategori_id)
    paginator = Paginator(posts, 10) 
    page = request.GET.get('page')
    if page == None :
        page = 1
        
    try:
        list_post = paginator.page(page)
    except PageNotAnInteger:
        list_post = paginator.page(1)
    except EmptyPage:
        list_post = paginator.page(paginator.num_pages)    
    
    return render_to_response('blog/kategori.html',{
        'posting' : list_post, 
        'kategori' : kat,
        },context_instance=RequestContext(request))