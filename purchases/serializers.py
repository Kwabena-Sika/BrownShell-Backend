from rest_framework import serializers
from .models import Purchase, PurchaseItem

class PurchaseSerialiazer(serializers.ModelSerializer):
    owed = serializers.ReadOnlyField()
    class Meta:
        model = Purchase
        fields = "__all__"

class PurchaseItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseItem
        fields = "__all__"