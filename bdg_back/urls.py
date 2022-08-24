from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from account.api.viewsets import MyTokenObtainPairView

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

schema_view = get_schema_view(
   openapi.Info(
      title="BDG API",
      default_version='v1',
      description="Api para o sistema de vendas do BDG",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=False,
   permission_classes=[permissions.IsAdminUser,]
)
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
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
if settings.DEBUG:
   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
