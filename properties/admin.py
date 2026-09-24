from django.contrib import admin

from .models import Property


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'location',
        'property_type',
        'price',
        'agent',
        'created_at',
    )
    list_filter = ('property_type', 'created_at')
    search_fields = ('title', 'location', 'description', 'agent__name')
