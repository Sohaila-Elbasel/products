from rest_framework import serializers
from . import models


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = ('id', 'name', 'serial_number', 'description', 'price', 'category')
        extra_kwargs = {'category': {'required': False}}


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = models.Category
        fields = ('id', 'name', 'products')
        extra_kwargs = {'products': {'required': False}}
