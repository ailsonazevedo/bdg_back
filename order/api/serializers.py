from rest_framework import serializers

from ..models import Order, OrderItem, Payment, Region

class OrderSerializer(serializers.ModelSerializer):
    #order_items = serializers.ListSerializer(many=False, queryset=OrderItem.objects.all())
    class Meta:
        model = Order
        fields = ['id', 'full_name','address', 'zipcode', 'number', 'district', 'complement', 'region', 'phone', 'status', 'get_status_choices', 'get_order_items']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'
