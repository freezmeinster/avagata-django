from django.db import models

class LandingConfig(models.Model):
    key = models.CharField(max_length=20)
    value = models.CharField(max_length=20)
    
    class Meta:
        verbose_name_plural = "Daftar Konfigurasi"
    
    def __unicode__(self):
        return self.key
