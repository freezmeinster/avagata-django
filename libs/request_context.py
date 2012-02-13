import datetime
from blog.models import Kategori
from landing.models import HalamanStatis,Kategori
from event.models import Event

def kategori_list(request):
    l_kategori = Kategori.objects.all()
    return { 'kategori_list' : l_kategori }

def feature_list(request):
    try :
        kate = Kategori.objects.get(nama="feature")
        f_list = HalamanStatis.objects.filter(kategori=kate.id)
    except :
        f_list = None
    
    return { 'feature_list' : f_list }
    
def now_event(request):
    today = datetime.datetime.today()
    now = Event.objects.filter(
        tanggal=today
        ).filter(
        status=True
        )
    return { 'now_event' : now }
    
def up_coming_event(request):
    today = datetime.datetime.today()
    now = Event.objects.filter(
        tanggal__gt=today
        ).filter(
        status=True
        )
    return { 'up_coming_event' : now }
