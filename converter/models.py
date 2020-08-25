from django.db import models
from btndom.helpers import model_helper
from btndom.helpers.choices import extension_choices, status_choices
# Create your models here.

class ConverterModel(model_helper.SimpleModel):
    media = models.FileField(blank=True, upload_to='converter_folder/')
    uploaded_extension = models.CharField(choices=extension_choices.EXTENSION_CHOICES, max_length=5)
    output_extension = models.CharField(choices=extension_choices.EXTENSION_CHOICES, max_length=5)
    output = models.TextField(blank=True)
    status = models.CharField(choices=status_choices.STATUS_CHOICES, max_length=20, default=status_choices.STATUS_CHOICES[2][0])


    def __str__(self):
        return f'{self.name} - {self.status}'
    
    @property
    def get_output_path(self):
        return f"{self.output.url}"

    @property
    def get_media_path(self):
        return f"{self.media.url}"

    @property
    def get_status(self):
        return f'{self.get_status_display()}'
