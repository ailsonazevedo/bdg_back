from rest_framework import serializers
from ..models import Category, Products


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'get_absolute_url','icon']

class ProductSerializer(serializers.ModelSerializer):
    #categoria = CategorySerializer(read_only=True)
    class Meta:
        model = Products
        fields = ['id', 'name', 'description', 'price', 'image', 'get_absolute_url', 'categoria', 'is_offer', 'active']