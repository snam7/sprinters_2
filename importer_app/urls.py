from django.urls import path
from . import views

app_name = 'importer_app'
urlpatterns = [
    path('importers/', views.importer_list, name='importer_list'),
]
