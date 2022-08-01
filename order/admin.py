from django.contrib import admin
from .models import Order, OrderItem, Region, Payment
# Register your models here.
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'price', 'created_at')
    list_filter = ('product', 'quantity', 'price', 'created_at')
    search_fields = ('product', 'quantity', 'price', 'created_at')

    fieldsets = (
        ('OrderItem', {
            'fields': ('product', 'quantity', 'price','note')
        }),
    )
    class Meta:
        model = OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('full_name','address', 'zipcode', 'number', 'district', 'complement', 'region', 'payment', 'phone', 'status', 'get_order_items')
    list_filter = ('full_name','address', 'zipcode', 'number', 'district', 'complement', 'region', 'payment', 'phone', 'status')
    search_fields = ('full_name','address', 'zipcode', 'number', 'district', 'complement', 'region', 'payment', 'phone', 'status')

    

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'shipping_price',)
    list_filter = ('name', 'shipping_price',)
    search_fields = ('name', 'shipping_price',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('name','description')
    list_filter = ('name', 'description')
    search_fields = ('name', 'description')