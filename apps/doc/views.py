from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from landing.models import LandingConfig,Testimoni
from random import randint
from doc.models import Media, KategoriHalaman, HalamanDoc

def install(request):
  
  