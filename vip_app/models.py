from django.db import models
from customer_app.models import Customer

class VIPCustomer(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    extra_discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.10)

    def __str__(self):
        return f"VIP {self.customer.username}"
