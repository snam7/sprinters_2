from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import MenuItem, CartItem, Cart
from .forms import OrderForm  # Assuming this form exists
from django.db.models import Count

@login_required
def add_to_cart(request, item_id):
    item = MenuItem.objects.get(id=item_id)
    cart, created = Cart.objects.get_or_create(user=request.user)  # Ensure the cart exists
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
    cart, created = Cart.objects.get_or_create(user=request.user)  # Ensure the cart exists
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'store_app/cart.html', {'cart_items': cart_items})

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart=request.user.cart)
    cart_item.delete()
    return redirect('store_app:view_cart')

def menu(request):
    items = MenuItem.objects.filter(is_available=True).order_by('name')
    return render(request, 'store_app/menu.html', {'menu_items': items})

# Example homepage view
def home(request):
    dishes = MenuItem.objects.annotate(order_count=Count('order_items')).order_by('-order_count')[:3]
    return render(request, 'store_app/home.html', {'dishes': dishes})

# Additional necessary views like about, checkout, etc.

def about(request):
    return render(request, 'store_app/about.html')

@login_required
def checkout(request):
    if request.method == 'POST':
        # Process the payment and complete the order
        # This is just a placeholder logic
        return redirect('store_app:order_confirmation')
    else:
        cart_items = CartItem.objects.filter(user=request.user)
        total = sum(item.menu_item.price * item.quantity for item in cart_items)
        return render(request, 'store_app/checkout.html', {'cart_items': cart_items, 'total': total})