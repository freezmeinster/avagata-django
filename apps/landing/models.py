from django.db import models

class LandingConfig(models.Model):
    key = models.CharField(max_length=20)
    value = models.TextField()
    
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
    

class Kategori(models.Model):
    nama = models.CharField(max_length=255)
    
    class Meta :
	verbose_name_plural = "Daftar Kategori Halaman"
	
    def __unicode__(self):
	return self.nama

class HalamanStatis(models.Model):
    judul = models.CharField(max_length=255)
    konten = models.TextField()
    kategori = models.ForeignKey(Kategori)
    tgl_edit = models.DateField(auto_now=True)
    
    class Meta :
	verbose_name_plural = "Daftar Halaman Statis"
	
    def __unicode__(self):
	return self.judul