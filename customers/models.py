from django.db import models

# Create your models here.

class Customer(models.Model):
    CATEGORY_CHOICES = [
        ("vendor", "Vendor"),
        ("school", "School"),
        ("hotel", "Hotel"),
        ("restaurant", "Restaurant"),
        ("other", "Other")
    ]

    STATUS_CHOICES = [
        ("active", "Active"),
        ("inactive", "Inactive")
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    phone = models.CharField(max_length=20)
    owed = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    location = models.CharField(max_length=200)
    last_purchase = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,default="active")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name