from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'address', 'joined', 'created_at', 'updated_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    readonly_fields = ('joined', 'created_at', 'updated_at')

    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'email', 'phone', 'address', 'image')
        }),
        ('Important dates', {
            'fields': ('joined', 'created_at', 'updated_at')
        }),
    )

admin.site.register(Customer, CustomerAdmin)
