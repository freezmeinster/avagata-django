from django.db import models

class LandingConfig(models.Model):
    key = models.CharField(max_length=20)
    value = models.CharField(max_length=20)
    
    class Meta:
        verbose_name_plural = "Daftar Konfigurasi"
    
    def __unicode__(self):
        return self.key
        

class Testimoni(models.Model):
    konten = models.TextField()
    pengirim = models.CharField(max_length=255)
    perusahaan = models.CharField(max_length=255,blank=True,null=True)
    
    def __unicode__(self):
	return self.konten

    class Meta :
	verbose_name_plural = "Daftar Testimoni"
    
