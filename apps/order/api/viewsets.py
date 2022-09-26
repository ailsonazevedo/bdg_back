from collections import _OrderedDictItemsView
from typing import OrderedDict
from django.http import response
from rest_framework.exceptions import NotFound
from ..models import Region, Payment, Additional, Order, OrderItem
from .serializers import RegionSerializer, PaymentSerializer, OrderSerializer, OrderItemSerializer

from rest_framework import status
from rest_framework import viewsets, permissions
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

class OrderViewsets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticated,)

class OrderItemViewsets(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = (permissions.IsAuthenticated,)

class PaymentViewsets(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class RegionViewsets(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)