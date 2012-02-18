from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from landing.models import LandingConfig,Testimoni,HalamanStatis
from random import randint

def home(request):
    l_config = LandingConfig.objects.get(key='under_maintenance')
    if l_config.value == "True":
        return render_to_response('index.html')
    else :
        return redirect('/landing')
    
def index(request):
    c_testis = Testimoni.objects.count()
    if c_testis != 0 :
        t_id = randint(1,c_testis)
        testis = Testimoni.objects.get(id=t_id)
    else : 
        testis = None
    return render_to_response('landing/home.html',{
	'testimoni' : testis,
	},context_instance=RequestContext(request))

def static(request):
    return render_to_response('index.html')

def read_feature(request,feature_id):
    halaman = HalamanStatis.objects.get(id=feature_id)
    return render_to_response('landing/read.html',{
	'halaman' : halaman,
	},context_instance=RequestContext(request))

def about_us(request):
  try :
    about_us=HalamanStatis.objects.get(kategori__nama='About')
  except :
    about_us=None
  return render_to_response('landing/about_us.html',{
    'about_us':about_us,
    }, context_instance=RequestContext(request))
    
def download(request):
  try :
    download=HalamanStatis.objects.get(kategori__nama='Download')
  except :
    download=None
  return render_to_response('landing/download.html',{
    'download':download,
    }, context_instance=RequestContext(request))