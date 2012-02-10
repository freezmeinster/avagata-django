from blog.models import Kategori

def kategori_list(request):
    l_kategori = Kategori.objects.all()
    return { 'kategori_list' : l_kategori }
