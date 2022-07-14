from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price', 'status', 'created_at')
    list_filter = ('order', 'product', 'quantity', 'price', 'status', 'created_at')
    search_fields = ('order', 'product', 'quantity', 'price', 'status', 'created_at')
    # ordering = ('product', 'quantity', 'price', 'total')
    fieldsets = (
        ('OrderItem', {
            'fields': ('order', 'product', 'quantity', 'price', 'status')
        }),
    )
    class Meta:
        model = OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'address', 'zipcode', 'place')
    list_display = ('full_name', 'email', 'phone', 'address', 'zipcode', 'place')
    search_fields = ('full_name', 'email', 'phone', 'address', 'zipcode', 'place')