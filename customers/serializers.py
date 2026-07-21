from rest_framework import serializers
from .models import  Customer

class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
        read_only_fields = (
            "id",
            "created_at",
            "updated_at"
        )