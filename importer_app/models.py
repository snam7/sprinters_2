from django.db import models

class Importer(models.Model):
    name = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.product_type})"
