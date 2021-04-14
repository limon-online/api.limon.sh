from django.contrib import admin
from django.contrib.auth.models import Group

from .models import User


admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'first_name',
        'last_name',
        'is_active',
        'last_login'
    )
    fieldsets = (
        ('General', {
            'fields': (
                'first_name', 'last_name', 'email', 'password'
            )
        }),
        ('Advanced options', {
            'fields': (
                'is_active', 'is_superuser', 'is_staff', 'created_at'
            ),
        }),
    )
    readonly_fields = (
        'created_at',
    )
    ordering = (
        '-created_at',
    )
    search_fields = (
        'first_name', 'last_name', 'email'
    )
    list_filter = (
        'is_active',
        'is_staff'
    )
