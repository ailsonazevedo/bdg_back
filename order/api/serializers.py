from rest_framework import serializers
from ..models import Order, OrderItem, Payment, Region

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name', 'shipping_price']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'price', 'created_at','note']

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ['id', 'full_name','address', 'zipcode', 'number', 'district', 'complement', 'region', 'payment', 'phone', 'status', 'get_status_choices', 'order_items']

