# Create your views here.
from django.shortcuts import render_to_response,redirect
from landing.models import LandingConfig

def index(request):
    l_config = LandingConfig.objects.get(key='under_maintenance')
    if l_config.value == "True":
        return render_to_response('index.html')
    else :
        return redirect('/landing')
    
def landing(request):
    return render_to_response('landing.html')
