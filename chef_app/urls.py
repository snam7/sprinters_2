from django.urls import path
from . import views

app_name = 'chef_app'
urlpatterns = [
    path('chefs/', views.chef_list, name='chef_list'),
]
