
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='customer_app/login.html'), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('account/', views.account, name='account'),
    path('place_order/', views.place_order, name='place_order'),
    path('orders/', views.order_list, name='order_list'),

]
