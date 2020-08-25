from django.contrib import admin
from .models import ConverterModel
# Register your models here.

@admin.register(ConverterModel)
class ConverterModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'uploaded_extension', 'output_extension', 'status']