from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class PerformanceReview(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='performance_reviews')
    date = models.DateField()
    rating = models.IntegerField()  # Assume 1-5 rating scale
    comments = models.TextField()

    def __str__(self):
        return f"Performance review for {self.employee.username}"
