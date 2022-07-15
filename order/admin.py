from django.contrib import admin
from .models import Order, OrderItem, Region
# Register your models here.
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price', 'status', 'created_at')
    list_filter = ('order', 'product', 'quantity', 'price', 'status', 'created_at')
    search_fields = ('order', 'product', 'quantity', 'price', 'status', 'created_at')

    fieldsets = (
        ('OrderItem', {
            'fields': ('order', 'product', 'quantity', 'price', 'status')
        }),
    )
    class Meta:
        model = OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('address', 'zipcode', 'number', 'district', 'complement', 'region')
    list_filter = ('address', 'zipcode', 'number', 'district', 'complement', 'region')
    search_fields = ('address', 'zipcode', 'number', 'district', 'complement', 'region')

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'shipping_price',)
    list_filter = ('name', 'shipping_price',)
    search_fields = ('name', 'shipping_price',)