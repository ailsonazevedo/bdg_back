from django.contrib import admin
from .models import Ordered, Products, Category

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'image', 'categoria')
    list_filter = ('name', 'description', 'price', 'image','categoria')
    search_fields = ('name', 'description', 'price', 'image')
    ordering = ('name', 'description', 'price', 'image')
    fieldsets = (
        ('Product', {
            'fields': ('name', 'description', 'price', 'image','categoria')
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
    class Meta:
        model = Products

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    fieldsets = (
        ('Category', {
            'fields': ('name',)
        }),
    )
    class Meta:
        model = Category

@admin.register(Ordered)
class OrderedAdmin(admin.ModelAdmin):
    list_display = ('products', 'quantity', 'price', 'total')
    list_filter = ('product', 'quantity', 'price')
    search_fields = ('product', 'quantity', 'price', 'total')
    # ordering = ('product', 'quantity', 'price', 'total')
    fieldsets = (
        ('Ordered', {
            'fields': ('product', 'quantity', 'price', 'total')
        }),
    )
    class Meta:
        model = Ordered
# Register your models here.
