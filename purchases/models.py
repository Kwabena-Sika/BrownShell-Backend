from django.db import models
from suppliers.models import Suppliers
from inventory.models import EggType
# Create your models here.

class Purchases(models.Model):
    supplier = models.ForeignKey(Suppliers, on_delete=models.CASCADE, related_name="purchases")
    date = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def owed(self):
        return self.total - self.paid
    
    def __str__(self):
        return f"Purchase #{self.id} - {self.supplier.name}"
    
class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchases,on_delete=models.CASCADE, related_name='items')
    egg_type = models.ForeignKey(EggType, on_delete=models.CASCADE, related_name='purchase_items')
    quantity = models.PositiveIntegerField()
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        self.subtotal = self.quantity * self.cost_price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.egg_type} - {self.quantity}"