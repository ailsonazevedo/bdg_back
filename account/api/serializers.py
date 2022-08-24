from rest_framework import permissions, serializers, status
from django.contrib.auth.models import User

from account.models import Address, Client


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]
        extra_kwargs = {'password':{'write_only':True}}


class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    address = AddressSerializer(required=False, allow_null=True)

    class Meta:
        model = Client
        fields = [
            'id',
            'full_name',
            'email',
            'phone',
            'address',
            'user'
        ]
    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        client = Client.objects.create(user=user, **validated_data)
        return client


class UpdateClientSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True)
    class Meta:
        model = Client
        fields = [
            "id",
            "full_name", 
            "email",
            "phone", 
            "address",
        ]

