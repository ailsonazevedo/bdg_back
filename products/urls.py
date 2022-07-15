from django.db import router
from django.urls import path
from rest_framework import urlpatterns
from products.api.viewsets import ProductsListView, CategoryListView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

urlpatterns = [
    path('products/', ProductsListView.as_view(), name='products'),
    path('category/', CategoryListView.as_view(), name='category'),
]

urlpatterns += router.urls