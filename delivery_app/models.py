from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class DeliveryPerson(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    delivery_zone = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
