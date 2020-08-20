from django.contrib import admin
from .models import DemoTS
# Register your models here.

@admin.register(DemoTS)
class DemoAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_ready', 'is_processing']