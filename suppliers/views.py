from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Suppliers
from .serializers import SupplierSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q


# Create your views here.
@api_view(["GET", "POST"])
def supplier_list(request):
    if request.method == "GET":
        suppliers = Suppliers.objects.all()

        search = request.query_params.get("search")
        if search:
            suppliers = suppliers.filter(
                Q(name__icontains=search) |
                Q(location__icontains=search) |
                Q(phone__icontains=search)
            )
        paginator = PageNumberPagination()
        paginated_supplier = paginator.paginate_queryset(suppliers, request)
        serializer = SupplierSerializer(paginated_supplier, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    elif request.method == "POST":
        serializer = SupplierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def supplier_stats(request):
    total_suppliers = Suppliers.objects.count()
    active_suppliers = Suppliers.objects.filter(status="active").count()
    inactive_suppliers = Suppliers.objects.filter(status="inactive").count()

    return Response({
        "total_suppliers": total_suppliers,
        "active_suppliers": active_suppliers,
        "inactive_suppliers": inactive_suppliers
    })


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