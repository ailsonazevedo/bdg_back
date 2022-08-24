from account.api.viewsets import ( 
    ClientDeleteViewSets, 
    ClientListViewSets, 
    ClientCreateViewSets, 
    ClientRetrieveUpdateViewSets, 
    ClientRetrieveViewSets,
    AddressViewSets,
)
from django.urls import path

from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'address', AddressViewSets)


urlpatterns =[
    path('clients/', ClientListViewSets.as_view(), name='client_list'),
    path('clients/<int:pk>', ClientRetrieveViewSets.as_view(), name='client_detail'),
    path('create-account-client', ClientCreateViewSets.as_view(), name='accounts_create'),
    path('update-account-client/<int:pk>', ClientRetrieveUpdateViewSets.as_view(), name='accounts_update'),
    path('delete-account-client/<int:pk>', ClientDeleteViewSets.as_view(), name='accounts_destroy'),
]

urlpatterns += router.urls