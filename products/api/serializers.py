from rest_framework import serializers
from ..models import Category, Products


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'name', 'description', 'price', 'image', 'categoria', 'get_absolute_url']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'get_absolute_url', 'get_absolute_url']