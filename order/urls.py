from rest_framework import urlpatterns
from .api.viewsets import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'order', OrderViewsets)
router.register(r'order_items', OrderItemViewsets)
router.register(r'region', RegionViewsets)
router.register(r'payment', PaymentViewsets)

urlpatterns = router.urls