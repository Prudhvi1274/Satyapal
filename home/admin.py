# from django.contrib import admin
# from .models import Theme, HomePageStructure

# Register your models here.

# @admin.register(Theme)
# class ThemeAdmin(admin.ModelAdmin):
#     """
#     Admin interface for the Theme model.
#     Organizes theme options into logical sections.
#     """
#     fieldsets = (
#         ('Color Scheme', {
#             'fields': ('primary_color', 'secondary_color'),
#         }),
#         ('Typography', {
#             'fields': ('font_family',),
#         }),
#     )


# @admin.register(HomePageStructure)
# class HomePageStructureAdmin(admin.ModelAdmin):
#     """Admin interface for managing the order of home page sections."""
#     list_display = ('section_name', 'order')
#     list_editable = ('order',)

# Note: Theme and Structure are now managed in the 'theme' app.
# This file is kept for reference but the code is commented out to avoid errors.
