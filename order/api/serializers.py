from rest_framework import serializers
from ..models import Order, OrderItem, Payment, Region
from products.api.serializers import ProductSerializer

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name', 'shipping_price']

class OrderItemSerializer(serializers.ModelSerializer):
    # product = ProductSerializer()
    class Meta:
        model = OrderItem
        fields = [
            'id', 
            'product', 
            'quantity', 
            'price', 
            'created_at',
            'note',
            'additional'
        ]

class OrderSerializer(serializers.ModelSerializer):
    # order_items = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = [
            'id', 
            'payment', 
            'status', 
            'order_items', 
            'get_status_choices',
            'user'
        ]

