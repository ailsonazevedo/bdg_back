from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from apps.account.api.serializers import AddressSerializer, ClientSerializer, UpdateClientSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.account.models import Address, Client

# List all clients 
class ClientListViewSets(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (permissions.IsAdminUser,)

# Create a new client
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
            )
            client.save()
            try:
                address = Address(
                    name=serializer.validated_data['address']['name'],
                    street=serializer.validated_data['address']['street'],
                    number=serializer.validated_data['address']['number'],
                    complement=serializer.validated_data['address']['complement'],
                    district=serializer.validated_data['address']['district'],
                    zipcode=serializer.validated_data['address']['zipcode'],
                    region=serializer.validated_data['address']['region'],
                    client=client
                )
                address.save()
            except Exception:
                pass

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientRetrieveViewSets(generics.RetrieveAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

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
    
    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return Client.objects.none()



class ClientRetrieveUpdateViewSets(generics.RetrieveUpdateAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

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
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientDeleteViewSets(generics.DestroyAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

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
        return Response({"message": "Successfully delete user!"},status=status.HTTP_204_NO_CONTENT)

class AddressViewSets(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return Address.objects.none()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        try:
            client = Client.objects.get(user=self.user)
            data["client_id"] = client.id
        except Exception as e:
            client = Client.objects.create(user=self.user, full_name=self.user.username)
            data["client_id"] = client.id

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer