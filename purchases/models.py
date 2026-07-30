from django.db import models
from suppliers.models import Suppliers
from inventory.models import EggType
# Create your models here.

class Purchase(models.Model):
    supplier = models.ForeignKey(Suppliers, on_delete=models.CASCADE)
    date = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name='items')
    egg_type = models.ForeignKey(EggType, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        self.subtotal = self.quantity * self.cost_price
        super().save(*args, **kwargs)

        self.purchase.total = sum(
            item.subtotal for item in self.purchase.items.all()
        )

        self.purchase.save()