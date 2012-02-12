from django.contrib import admin
from blog.models import Kategori, Post

class PostAdmin(admin.ModelAdmin):
    search_fields = ('judul','konten')
    list_display = ('judul', 'kategori', 'get_status','get_date','user')
    
    class Media:
        js = (
              '/asset/tiny_mce/tiny_mce.js',
              '/asset/textarea.js',)
    
    
admin.site.register(Kategori) 
admin.site.register(Post, PostAdmin)