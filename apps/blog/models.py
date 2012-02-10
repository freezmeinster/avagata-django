from django.db import models

class Kategori(models.Model):
    nama = models.CharField(max_length=255)
    
    def __unicode__(self):
	return self.nama

    class Meta :
	verbose_name_plural = "Daftar Kategori"