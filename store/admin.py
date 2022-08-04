from django.contrib import admin

from store.models import Store

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'state', 'zipcode', 'phone', 'email')
    list_filter = ('name', 'address', 'city', 'state', 'zipcode', 'phone', 'email')
    search_fields = ('name', 'address', 'city', 'state', 'zipcode', 'phone', 'email')
    ordering = ['name']
    fields = ('name', 'logo', 'address', 'city', 'state', 'zipcode', 'phone', 'email')
    readonly_fields = ('created_at', 'updated_at')
    class Meta:
        model = Store
        verbose_name_plural = 'Stores'
        verbose_name = 'Store'
