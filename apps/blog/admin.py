from django.contrib import admin
from blog.models import Kategori, Post, Event

class PostAdmin(admin.ModelAdmin):
    search_fields = ('judul','konten')
    list_display = ('judul', 'kategori', 'get_status','get_date','user')
    
    
admin.site.register(Kategori) 
admin.site.register(Post, PostAdmin)
admin.site.register(Event)