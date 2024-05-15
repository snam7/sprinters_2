
from django.urls import path
from . import views
from .views import add_to_cart, view_cart, remove_from_cart


urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('home/',views.home,name='home'),
    path('',views.home,name='home'),
    path('about/', views.about, name='about'),
    path('add-to-cart/<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='cart'),
    path('remove-from-cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout, name='checkout'),

]
    