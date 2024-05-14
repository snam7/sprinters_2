from django.shortcuts import render
from .models import DeliveryPerson

def delivery_list(request):
    delivery_people = DeliveryPerson.objects.all()
    return render(request, 'delivery_app/delivery_list.html', {'delivery_people': delivery_people})
