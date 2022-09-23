from django.contrib import admin
from .models import Address, Client
from django.contrib.admin.models import LogEntry

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'email', 'full_name', 'phone')
    list_filter = ('user', 'email', 'full_name', )
    search_fields = ('user', 'email', 'full_name', 'phone',)

    fieldsets = (
        ('Profile', {
            'fields': ('user', 'email', 'full_name', 'phone')
        }),
    )
    class Meta:
        model = Client

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id','name','street', 'number', 'complement', 'district', 'zipcode', 'region', 'user')
    list_filter = ('street', 'number', 'complement', 'district', 'zipcode', 'region')
    search_fields = ('street', 'number', 'complement', 'district', 'zipcode', 'region')

    fieldsets = (
        ('Address', {
            'fields': ('name','street', 'number', 'complement', 'district', 'zipcode', 'region', 'user')
        }),
    )
    class Meta:
        model = Address

@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    # to have a date-based drilldown navigation in the admin page
    date_hierarchy = 'action_time'

    # to filter the resultes by users, content types and action flags
    list_filter = [
        'user',
        'content_type',
        'action_flag'
    ]

    # when searching the user will be able to search in both object_repr and change_message
    search_fields = [
        'object_repr',
        'change_message'
    ]

    list_display = [
        'action_time',
        'user',
        'content_type',
        'action_flag',
    ]
    readonly_fields = [
        'action_time',
        'user',
        'content_type',
        'object_id',
        'object_repr',
        'action_flag',
        'change_message'
    ]
# Register your models here.
