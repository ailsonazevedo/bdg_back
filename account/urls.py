from account.api.viewsets import (
    AddressRetrieveUpdateViewSets, 
    ClientDeleteViewSets, 
    ClientListViewSets, 
    ClientCreateViewSets, 
    ClientRetrieveUpdateViewSets, 
    ClientRetrieveViewSets
)
from django.urls import path

urlpatterns =[
    path('clients/', ClientListViewSets.as_view(), name='client_list'),
    path('clients/<int:pk>', ClientRetrieveViewSets.as_view(), name='client_detail'),
    path('create-account-client', ClientCreateViewSets.as_view(), name='accounts_create'),
    path('update-account-client/<int:pk>', ClientRetrieveUpdateViewSets.as_view(), name='accounts_update'),
    path('delete-account-client/<int:pk>', ClientDeleteViewSets.as_view(), name='accounts_destroy'),
    path('update-address-client/<int:pk>', AddressRetrieveUpdateViewSets.as_view(), name='address_update'),
]