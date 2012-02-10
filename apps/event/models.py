from django.db import models

# Create your models here.
class Event(models.Model):
    nama = models.CharField(max_length=200)
    tanggal = models.DateField()
    tempat = models.CharField(max_length=200)
    keterangan = models.TextField()
    status = models.BooleanField()
    
    def __unicode__(self):
	return self.nama