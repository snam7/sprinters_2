
from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('',views.home,name='home'),
    path('about/', views.about, name='about'),

]
    