from django.db import models
from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser):
    vip_status = models.BooleanField(default=False)
    
    # Specify unique related names for the groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='customer_groups'  # New related_name
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='customer_permissions'  # New related_name
    )

    def is_vip(self):
        return self.vip_status


