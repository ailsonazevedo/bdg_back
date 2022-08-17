from django.contrib import admin
from .models import Client
@admin.register(Client)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'phone', 'address', 'zipcode', 'number', 'district', 'complement','region')
    list_filter = ('user', 'full_name', 'phone', 'address', 'zipcode', 'number', 'district', 'complement','region')
    search_fields = ('user', 'full_name', 'phone', 'address', 'zipcode', 'number', 'district', 'complement')

    fieldsets = (
        ('Profile', {
            'fields': ('user', 'full_name', 'phone', 'address', 'zipcode', 'number', 'district', 'complement','region')
        }),
    )
    class Meta:
        model = Client
# Register your models here.
