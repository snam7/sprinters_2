from django.shortcuts import render
from .models import Feedback

def feedback_list(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'feedback_app/feedback_list.html', {'feedbacks': feedbacks})
