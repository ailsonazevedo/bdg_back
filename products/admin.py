from django.contrib import admin
from .models import Products, Category

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


# Register your models here.
