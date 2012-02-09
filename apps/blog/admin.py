from django.contrib import admin
from blog.models import Kategori, Post, Event

class PostAdmin(admin.ModelAdmin):
    list_display = ('judul', 'pub_date')
    
    
admin.site.register(Kategori) 
admin.site.register(Post, PostAdmin)
admin.site.register(Event)