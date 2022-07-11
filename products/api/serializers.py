from rest_framework import serializers
from models import Category
from products.models import Products


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products, Category
        fields = ['id', 'name', 'description', 'price', 'image', 'categoria']

