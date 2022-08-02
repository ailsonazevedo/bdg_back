from django.contrib import admin
from .models import Products, Category

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'image', 'categoria','is_offer','active')
    list_filter = ('name', 'description', 'price', 'image','categoria','is_offer','active')
    search_fields = ('name', 'description', 'price', 'image','is_offer')
    ordering = ('name', 'description', 'price', 'image')
    fieldsets = (
        ('Product', {
            'fields': ('name', 'description', 'price', 'image','categoria','is_offer','active')
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
            'fields': ('name','icon')
        }),
    )
    class Meta:
        model = Category


# Register your models here.
