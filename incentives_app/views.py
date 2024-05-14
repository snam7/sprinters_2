from django.shortcuts import render
from .models import Incentive

def incentive_list(request):
    incentives = Incentive.objects.all()
    return render(request, 'incentives_app/incentive_list.html', {'incentives': incentives})
