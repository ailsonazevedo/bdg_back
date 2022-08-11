from django.contrib import admin
from .models import Profile
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'phone', 'address', 'zipcode', 'number', 'district', 'complement')
    list_filter = ('user', 'full_name', 'phone', 'address', 'zipcode', 'number', 'district', 'complement')
    search_fields = ('user', 'full_name', 'phone', 'address', 'zipcode', 'number', 'district', 'complement')

    fieldsets = (
        ('Profile', {
            'fields': ('user', 'full_name', 'phone', 'address', 'zipcode', 'number', 'district', 'complement')
        }),
    )
    class Meta:
        model = Profile
# Register your models here.
