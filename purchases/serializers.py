from rest_framework import serializers
from .models import Purchases, PurchaseItem

class PurchaseSerialiazer(serializers.ModelSerializer):
    owed = serializers.ReadOnlyField()
    class Meta:
        model = Purchases
        fields = "__all__"

class PurchaseItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseItem
        fields = "__all__"