from django.shortcuts import render
from .models import PerformanceReview

def performance_review_list(request):
    reviews = PerformanceReview.objects.all()
    return render(request, 'performance_app/performance_review_list.html', {'reviews': reviews})
