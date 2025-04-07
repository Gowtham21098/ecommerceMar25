from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from products.models import Products
from rest_framework.decorators import api_view

from products.serializers import ProductSerializer


# Create your views here.
def hello(request):
    data = Products.objects.all()
    print(data[0].name)
    data[0].name = 'abc'
    print(data[0].name)
    return HttpResponse('Hello World!, Have a good day')

@api_view(['GET'])
def get_products(request):
    data = Products.objects.all()
    serializedProducts = ProductSerializer(data, many=True)
    return Response(serializedProducts.data)


@api_view(['GET'])
def get_product(request,id):
    try:
        data = Products.objects.get(id=id)
        serializedProducts = ProductSerializer(data)
        return Response(serializedProducts.data)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

