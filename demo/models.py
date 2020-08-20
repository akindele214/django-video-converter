from django.db import models

# Create your models here.

class DemoTS(models.Model):
    name = models.CharField(max_length=25)
    media = models.FileField(upload_to='demo/')
    is_ready = models.BooleanField(default=False)
    is_processing = models.BooleanField(default=False)
    download_url = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name} - {self.is_ready}'
    
    @property
    def size(self):
        return self.media.size