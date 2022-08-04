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

class StoreViewsets(viewsets.ModelViewSet):
    
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)  



