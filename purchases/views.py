from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Purchases
from .serializers import PurchaseSerialiazer
from rest_framework.response import Response
from rest_framework import status
from .models import PurchaseItem
from .serializers import PurchaseItemSerializer
# Create your views here.


@api_view(["GET", "POST"])

def purchase_list(request):
    if request.method == "GET":
        purchases = Purchases.objects.all()
        serializer = PurchaseSerialiazer(purchases, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = PurchaseSerialiazer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET","PUT", "DELETE"])
def purchase_detail(request, id):
    try:
        purchase = Purchases.objects.get(id=id)
    except Purchases.DoesNotExist:
        return Response(
            {"error": "Purchase not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    if request.method == "GET":
        serializer = PurchaseSerialiazer(purchase)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = PurchaseSerialiazer(purchase, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        purchase.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET", "POST"])
def purchase_item_list(request):
    if request.method == "GET":
        items = PurchaseItem.objects.all()
        serializer = PurchaseItemSerializer(items, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = PurchaseItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def purchase_item_detail(request, id):
    try:
        item = PurchaseItem.objects.get(id=id)
    except PurchaseItem.DoesNotExist:
        return Response(
            {"error": "Purchase item not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    if request.method == "GET":
        serializer = PurchaseItemSerializer(item)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = PurchaseItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)