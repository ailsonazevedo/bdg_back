from django.contrib import admin
from .models import Address, Client
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'email', 'full_name', 'phone','address')
    list_filter = ('user', 'email', 'full_name', )
    search_fields = ('user', 'email', 'full_name', 'phone',)

    fieldsets = (
        ('Profile', {
            'fields': ('user', 'email', 'full_name', 'phone','address')
        }),
    )
    class Meta:
        model = Client

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id','name','street', 'number', 'complement', 'district', 'zipcode', 'region')
    list_filter = ('street', 'number', 'complement', 'district', 'zipcode', 'region')
    search_fields = ('street', 'number', 'complement', 'district', 'zipcode', 'region')

    fieldsets = (
        ('Address', {
            'fields': ('name','street', 'number', 'complement', 'district', 'zipcode', 'region')
        }),
    )
    class Meta:
        model = Address
# Register your models here.
