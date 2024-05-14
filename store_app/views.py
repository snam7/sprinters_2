
from django.shortcuts import render
from .models import MenuItem
from django.db.models import Count
from . import views


def menu(request):
    items = MenuItem.objects.filter(is_available=True)
    return render(request, 'store_app/menu.html', {'menu_items': items})

from django.shortcuts import render
from .models import MenuItem

def home(request):
    if request.user.is_authenticated and hasattr(request.user, 'customer'):
        # Tailor content for logged-in users
        dishes = MenuItem.objects.annotate(
        orders_count=Count('order_items')
    ).order_by('-orders_count')[:3]
    else:
        # Content for visitors
        dishes = MenuItem.objects.order_by('-order_count')[:3]  # Most ordered dishes
    return render(request, 'store_app/home.html', {'dishes': dishes})

def home_view(request):
    # Get the top 3 most ordered menu items
    dishes = MenuItem.objects.annotate(order_count=Count('order_items')).order_by('-order_count')[:3]
    context = {'dishes': dishes}
    return render(request, 'store_app/home.html', context)

def about(request):
    return render(request, 'store_app/about.html')