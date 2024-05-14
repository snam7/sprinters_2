from django.shortcuts import render
from .models import Chef

def chef_list(request):
    chefs = Chef.objects.all()
    return render(request, 'chef_app/chef_list.html', {'chefs': chefs})
