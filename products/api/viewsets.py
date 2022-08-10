from collections import _OrderedDictItemsView
from typing import OrderedDict
from django.http import response
from rest_framework.exceptions import NotFound
from ..models import *
from .serializers import *

from rest_framework import status
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

# Create your views here.

class ProductsViewsets(viewsets.ModelViewSet):
    
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)  

class CategoryViewsets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class OffersViwesets(viewsets.ModelViewSet):
    queryset = Products.objects.filter(is_offer=True).order_by('updated_at')
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
