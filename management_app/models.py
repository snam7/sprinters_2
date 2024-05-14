from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level = models.IntegerField(default=1)

    def __str__(self):
        return f"Manager {self.user.username}"
