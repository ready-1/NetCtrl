from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('notify_on_approval',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('notify_on_approval',)}),
    )
    list_display = UserAdmin.list_display + ('notify_on_approval',)

# admin.site.register(CustomUser, UserAdmin)



