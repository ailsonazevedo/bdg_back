from rest_framework import serializers
from models import Category, Products


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products, Category
        fields = ['id', 'name', 'description', 'price', 'image', 'categoria']

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'get_absolute_url', 'products']