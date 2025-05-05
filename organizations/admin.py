from django.contrib import admin
from .models import Organization

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'is_verified', 'created_at')
    list_filter = ('is_verified', 'created_at')
    search_fields = ('name', 'user__username', 'registration_number')
    list_editable = ('is_verified',)  # Allow quick editing of verification status
    actions = ['verify_organizations', 'unverify_organizations']

    def verify_organizations(self, request, queryset):
        queryset.update(is_verified=True)
    verify_organizations.short_description = "Mark selected organizations as verified"

    def unverify_organizations(self, request, queryset):
        queryset.update(is_verified=False)
    unverify_organizations.short_description = "Mark selected organizations as unverified"