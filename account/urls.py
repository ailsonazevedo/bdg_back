from account.api.viewsets import ClientDeleteViewSets, ClientListViewSets, ClientCreateViewSets, ClientRetrieveUpdateViewSets
from django.urls import path

urlpatterns =[
    path('clients/', ClientListViewSets.as_view(), name='client_list'),
    path('create-account', ClientCreateViewSets.as_view(), name='accounts_create'),
    path('update-account-client/<int:pk>', ClientRetrieveUpdateViewSets.as_view(), name='accounts_update'),
    path('delete-account/<int:pk>', ClientDeleteViewSets.as_view(), name='accounts_destroy'),
]