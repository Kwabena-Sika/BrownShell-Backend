from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Suppliers
from .serializers import SupplierSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
@api_view(["GET", "POST"])
def supplier_list(request):
    if request.method == "GET":
        suppliers = Suppliers.objects.all()
        serializer = SupplierSerializer(suppliers, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = SupplierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def supplier_detail(request, id):
    try:
        supplier = Suppliers.objects.get(id=id)
    except Suppliers.DoesNotExist:
        return Response(
            {"error": "Supplier not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    
    if request.method == "GET":
        serializer = SupplierSerializer(supplier)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = SupplierSerializer(supplier, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        supplier.delete()
        return Response(
            {"message": "Supplier deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )