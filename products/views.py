from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from products.CustomException import ProductOutOfStockException
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
        if not data:
            raise ProductOutOfStockException("Product not found")
        print(data)
        serializedProducts = ProductSerializer(data)
        return Response(serializedProducts.data)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except ProductOutOfStockException as e:
        print(1)
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Exception as ee:
        print(2)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['POST'])
def create_product(request):
    try:
        data = request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serializer.data,status=status.HTTP_201_CREATED)
    except Exception as e:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
