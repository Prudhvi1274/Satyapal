from django.contrib import admin
from .models import ThemeSettings, StructureSettings

@admin.register(ThemeSettings)
class ThemeSettingsAdmin(admin.ModelAdmin):
    """
    Admin interface for managing the website's theme settings.
    """
    fieldsets = (
        ('Color Scheme', {
            'fields': ('primary_color', 'secondary_color'),
            'description': "Define the main colors for the website's theme."
        }),
        ('Typography', {
            'fields': ('font',),
            'description': "Select the primary font for the website."
        }),
    )

    def has_add_permission(self, request):
        # Prevent adding new ThemeSettings if one already exists
        return not ThemeSettings.objects.exists()

@admin.register(StructureSettings)
class StructureSettingsAdmin(admin.ModelAdmin):
    """
    Admin interface for managing the visibility of different sections on the website.
    """
    list_display = ('id', 'show_hero_section', 'show_features_section', 'show_about_section', 'show_services_section', 'show_contact_section')
    list_editable = ('show_hero_section', 'show_features_section', 'show_about_section', 'show_services_section', 'show_contact_section')

    def has_add_permission(self, request):
        # Prevent adding new StructureSettings if one already exists
        return not StructureSettings.objects.exists()
