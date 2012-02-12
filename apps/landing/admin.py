from django.contrib import admin
from landing.models import LandingConfig,Testimoni,Kategori,HalamanStatis


class AdminHalamanStatis(admin.ModelAdmin):
    class Media:
        js = (
              '/asset/tiny_mce/tiny_mce.js',
              '/asset/textarea.js',)
        
admin.site.register(Kategori)
admin.site.register(HalamanStatis,AdminHalamanStatis)
admin.site.register(LandingConfig)
admin.site.register(Testimoni)
