from collections import _OrderedDictItemsView
from typing import OrderedDict
from django.http import response
from rest_framework.exceptions import NotFound
from ..models import *
from .serializers import *

from rest_framework import status
from rest_framework import viewsets

from rest_framework.exceptions import NotFound
from rest_framework.response import Response

class OrderViewsets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

