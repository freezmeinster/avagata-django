from django.db import models

# Create your models here.
class Event(models.Model):
    nama = models.CharField(max_length=200)
    tanggal = models.DateField()
    keterangan = models.TextField()
    
    def __unicode__(self):
	return self.nama