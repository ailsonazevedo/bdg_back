from django.contrib import admin
from .models import Products

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'image')
    list_filter = ('name', 'description', 'price', 'image')
    search_fields = ('name', 'description', 'price', 'image')
    ordering = ('name', 'description', 'price', 'image')
    fieldsets = (
        ('Product', {
            'fields': ('name', 'description', 'price', 'image')
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
    class Meta:
        model = Products
# Register your models here.
