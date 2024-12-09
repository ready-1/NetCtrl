from django.contrib import admin
from .models import Switch

@admin.register(Switch)
class SwitchAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('name', 'ip_address_in_band', 'status', 'model', 'location', 'last_sync')
    
    # Fields to enable search functionality
    search_fields = ('name', 'ip_address_in_band', 'mac_address', 'model', 'serial_number', 'location')
    
    # Fields to filter results in the admin interface
    list_filter = ('status', 'model', 'location')
    
    # Default ordering of the list view
    ordering = ('name',)