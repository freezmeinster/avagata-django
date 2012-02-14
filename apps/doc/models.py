from django.db import models

class Media(models.Model):
    media = models.FileField()
    
    class Meta :
	verbose_name_plural = "Daftar Media"

    def get_image(self):
	file_name = self.media.url.split('/')[1]
	return "<img height='125' src='/media/%s'" % file_name
    get_image.short_description = 'Gambar' 
    get_image.allow_tags = True
    
    def get_url(self):
	file_name = self.media.url.split('/')[1]
	return "<a href='/media/%s'>Url</a>" % file_name
    get_url.short_description = 'Url' 
    get_url.allow_tags = True


class KategoriHalaman(models.Model):
    nama = models.CharField(max_length=255)
    
    class Meta :
	verbose_name_plural = "Daftar Kategori Dokumentasi"
    
    def __unicode__(self):
	return self.nama

class HalamanDoc(models.Model):
    judul = models.CharField(max_length=255)
    konten = models.TextField()
    tgl_edit = models.DateField(auto_now=True)
    kategori = models.ForeignKey(KategoriHalaman)
    
    class Meta :
	verbose_name_plural = "Daftar Dokumentasi"

    def __unicode__(self):
	return self.judul
