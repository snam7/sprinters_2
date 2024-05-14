from django.shortcuts import render
from .models import VIPCustomer

def vip_list(request):
    vips = VIPCustomer.objects.all()
    return render(request, 'vip_app/vip_list.html', {'vips': vips})
