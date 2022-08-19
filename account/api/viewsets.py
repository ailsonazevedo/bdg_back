from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from account.api.serializers import AddressSerializer, ClientSerializer, UpdateAddressSerializer, UpdateClientSerializer
from django.contrib.auth.models import User

from account.models import Address, Client

class ClientListViewSets(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (permissions.IsAuthenticated,)

class ClientCreateViewSets(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            nome_sobrenome = serializer.validated_data['full_name'].split(' ')
            if len(nome_sobrenome) < 2:
                nome_sobrenome.append(' ')
            
            senha = serializer.validated_data['user']['password']
            user = User.objects.create_user(
                username=serializer.validated_data['user']['username'],
                first_name=nome_sobrenome[0],
                last_name=nome_sobrenome[-1],
                is_staff=False,
                is_superuser=False,
                password=senha
            )
            client = Client(
                user=user,
                full_name=serializer.validated_data['full_name'],
                phone=serializer.validated_data['phone'],
                email=serializer.validated_data['email'],
                address=serializer.validated_data['address'],
                region=serializer.validated_data['region']
            )
            client.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientRetrieveViewSets(generics.RetrieveAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    permission_classes = (permissions.AllowAny,)

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        client = self.get_queryset().filter(pk=pk).first()

        serializer = ClientSerializer(
            instance=client,
            data=request.data,
            many=False,
            context={'request': request},
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
        )


class ClientRetrieveUpdateViewSets(generics.RetrieveUpdateAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    permission_classes = (permissions.AllowAny,)

    def get_object(self):
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(
            self.get_queryset(),
            pk=pk
        )
        self.check_object_permissions(self.request, obj)
        return obj

    def update(self, request, *args, **kwargs):
        client = self.get_object()

        serializer = UpdateClientSerializer(client, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientDeleteViewSets(generics.DestroyAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    permission_classes = (permissions.AllowAny,)

    def get_object(self):
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(
            self.get_queryset(),
            pk=pk
        )
        self.check_object_permissions(self.request, obj)
        return obj

    def destroy(self, request, *args, **kwargs):
        client = self.get_object()
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AddressRetrieveUpdateViewSets(generics.RetrieveUpdateAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    permission_classes = (permissions.AllowAny,)

    def get_object(self):
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(
            self.get_queryset(),
            pk=pk
        )
        self.check_object_permissions(self.request, obj)
        return obj

    def update(self, request, *args, **kwargs):
        address = self.get_object()

        serializer = UpdateAddressSerializer(address, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)