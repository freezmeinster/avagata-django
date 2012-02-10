 
from django.contrib import admin
from event.models import Event

class EventAdmin(admin.ModelAdmin):
    search_fields = ('nama','tanggal')
    list_display = ('nama', 'tanggal', 'keterangan')
    
    
admin.site.register(Event)