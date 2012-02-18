from django.contrib import admin 
from doc.models import Media,KategoriHalaman,HalamanDoc

class MediaAdmin(admin.ModelAdmin):
    list_display = ('media','get_image','get_url')

admin.site.register(Media,MediaAdmin)
admin.site.register(KategoriHalaman)
admin.site.register(HalamanDoc)
