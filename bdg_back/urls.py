from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from account.api.viewsets import MyTokenObtainPairView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from django.urls import (
    path, 
    include, 
    re_path,
)

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

#Admin Configs UI
admin.site.site_header = 'BDG Admin'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/', include('products.urls')),
    path('api/v1/', include('order.urls')),
    path('api/v1/', include('store.urls')),
    path('api/v1/', include('account.urls')),
    path('auth/', include('rest_framework.urls')),

    # Swagger urls
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
if settings.DEBUG:
   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
