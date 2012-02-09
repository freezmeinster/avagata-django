from django.db import models
from django.contrib.admin.models import User
class Kategori(models.Model):
    nama = models.CharField(max_length=255)
    
    def __unicode__(self):
	return self.nama

    class Meta :
	verbose_name_plural = "Daftar Kategori"

class Post(models.Model):
    pub_date = models.DateField(auto_now_add=True)
    judul = models.CharField(max_length=200)
    konten = models.TextField()
    status = models.BooleanField()
    user = models.ForeignKey(User)
    kategori = models.ForeignKey("Kategori")
    
    def __unicode__(self):
	return self.judul
   

class Event(models.Model):
    nama = models.CharField(max_length=200)
    tanggal = models.DateField()
    keterangan = models.TextField()
    
    def __unicode__(self):
	return self.nama