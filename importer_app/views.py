from django.shortcuts import render
from .models import Importer

def importer_list(request):
    importers = Importer.objects.filter(is_active=True)
    return render(request, 'importer_app/importer_list.html', {'importers': importers})
