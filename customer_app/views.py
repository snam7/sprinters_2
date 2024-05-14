
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomerRegistrationForm, CustomerProfileForm
from .models import Customer
from store_app.models import Order
from store_app.forms import OrderForm

def order_list(request):
    if not request.user.is_authenticated:
        return redirect('login')
    orders = Order.objects.filter(customer=request.user)
    return render(request, 'customer_app/order_list.html', {'orders': orders})

def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user
            order.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'customer_app/place_order.html', {'form': form})


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_app/customer_list.html', {'customers': customers})

def register(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('customer_app:account')
    else:
        form = CustomerRegistrationForm()
    return render(request, 'customer_app/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('customer_app:account')
        else:
            return render(request, 'customer_app/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'customer_app/login.html')

def user_logout(request):
    logout(request)
    return redirect('customer_app:login')

@login_required
def account(request):
    if request.method == 'POST':
        form = CustomerProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('customer_app:account')
    else:
        form = CustomerProfileForm(instance=request.user)
    return render(request, 'customer_app/account.html', {'form': form})