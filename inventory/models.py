from django.db import models

# Create your models here.
class EggType(models.Model):
    EGG_TYPE_CHOICES = [
        ("large", "Large"),
        ("medium", "Medium"),
        ("small", "Small")
    ]
    name = models.CharField(max_length=20, choices=EGG_TYPE_CHOICES, unique=True)
    
    def __str__(self):
        return self.get_name_display()
    
