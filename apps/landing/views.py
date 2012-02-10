from django.shortcuts import render_to_response,redirect
from landing.models import LandingConfig

def home(request):
    l_config = LandingConfig.objects.get(key='under_maintenance')
    if l_config.value == "True":
        return render_to_response('index.html')
    else :
        return redirect('/landing')
    
def index(request):
    return render_to_response('landing/home.html')

def static(request):
    return render_to_response('index.html')
