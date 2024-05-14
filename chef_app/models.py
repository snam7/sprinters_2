from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Chef(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience = models.IntegerField(default=0)
    speciality = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
