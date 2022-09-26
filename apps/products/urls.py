from django.db import router
from rest_framework import urlpatterns
from .api.viewsets import ProductsViewsets, CategoryViewsets, OffersViwesets
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'products', ProductsViewsets)
router.register(r'category', CategoryViewsets)
router.register(r'offers', OffersViwesets)

urlpatterns = router.urls