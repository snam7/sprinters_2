from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Incentive(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='incentives')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.TextField()
    date_awarded = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Incentive for {self.recipient.username} - ${self.amount}"
