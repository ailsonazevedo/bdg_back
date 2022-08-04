from django.db import router
from rest_framework import urlpatterns
from .api.viewsets import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'store', StoreViewsets)

urlpatterns = router.urls