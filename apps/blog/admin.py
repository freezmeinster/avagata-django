from django.contrib import admin
from blog.models import Kategori, Post, Event

admin.site.register(Kategori) 
admin.site.register(Post)
admin.site.register(Event)