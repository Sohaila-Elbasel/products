from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from . import models
from . import serializers


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'api Overview': '/api/v1/',
        'view categories': '/api/v1/category/',
        'add category': '/api/v1/category/add',
    }

    return Response(api_urls)


@api_view(['GET', 'POST'])
def category(request):
    if request.method == 'GET':
        categories = models.Category.objects.all()
        serialize = serializers.CategorySerializer(categories, many=True)

        return Response(serialize.data)

    elif request.method == 'POST':
        serialize = serializers.CategorySerializer(data=request.data)

        if serialize.is_valid():
            serialize.save()

            return Response(serialize.data, status=status.HTTP_201_CREATED)

        return Response({'message': 'category is not valid'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def edit_category(request, id):
    try:
        category = models.Category.objects.get(id=id)
    except:
        return Response({'message':'category not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serialize = serializers.CategorySerializer(category, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)

    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def product(request):
    if request.method == 'GET':
        products = models.Product.objects.all()
        serialize = serializers.ProductSerializer(products, many=True)

        return Response(serialize.data)

    elif request.method == 'POST':
        serialize = serializers.ProductSerializer(data=request.data)

        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)

        return Response({'message': 'product is not valid'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def edit_product(request, id):
    product = models.Product.objects.filter(id=id).first()
    if not product:
        return Response({'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serialize = serializers.ProductSerializer(product)
        return Response(serialize.data)

    elif request.method == 'PUT':
        serialize = serializers.ProductSerializer(product, data=request.data, partial=True)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data )
        return Response({"message": 'Not valid'}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
