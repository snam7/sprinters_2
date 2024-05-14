from django.contrib import admin
from .models import Importer

@admin.register(Importer)
class ImporterAdmin(admin.ModelAdmin):
    list_display = ['name', 'product_type', 'is_active']
