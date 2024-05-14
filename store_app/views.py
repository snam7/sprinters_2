
from .models import MenuItem
from django.db.models import Count
from . import views
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import MenuItem, CartItem

@login_required
def add_to_cart(request, item_id):
    item = MenuItem.objects.get(id=item_id)
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user, 
        menu_item=item,
        defaults={'quantity': 1}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('store_app:menu')

@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'store_app/cart.html', {'cart_items': cart_items})

@login_required
def remove_from_cart(request, item_id):
    CartItem.objects.filter(id=item_id, user=request.user).delete()
    return redirect('store_app:view_cart')


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