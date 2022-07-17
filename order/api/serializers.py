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
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False, read_only=True)
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'price', 'created_at']

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)
    #regions = RegionSerializer(read_only=True)
    #payment = PaymentSerializer(read_only=True)
    class Meta:
        model = Order
        fields = ['id', 'full_name','address', 'zipcode', 'number', 'district', 'complement', 'region', 'payment', 'phone', 'status', 'get_status_choices', 'order_items']

