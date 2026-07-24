from rest_framework import serializers
from .models import EggType

class EggTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = EggType
        fields = "__all__"