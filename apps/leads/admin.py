# apps/base/admin.py (or wherever your Lead model is)
from django.contrib import admin
from .models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'state', 'created_at', 'updated_at')
    list_filter = ('state', 'created_at')
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
