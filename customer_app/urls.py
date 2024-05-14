
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('account/', views.account, name='account'),
    path('place_order/', views.place_order, name='place_order'),
    path('orders/', views.order_list, name='order_list'),

]
