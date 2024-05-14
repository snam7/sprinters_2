from django.shortcuts import render
from .models import Manager

def manager_list(request):
    managers = Manager.objects.all()
    return render(request, 'management_app/manager_list.html', {'managers': managers})
