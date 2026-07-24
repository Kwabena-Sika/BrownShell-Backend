from django.shortcuts import render
from .models import EggType
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import EggTypeSerializers

# Create your views here.
@api_view(["GET", "POST"])
def egg_type_list(request):
    if request.method == "GET":
        egg_types = EggType.objects.all()
        serializer = EggTypeSerializers(egg_types, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = EggTypeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)