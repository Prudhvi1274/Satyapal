from django.contrib import admin
from .models import SiteContent

@admin.register(SiteContent)
class SiteContentAdmin(admin.ModelAdmin):
    """
    Admin configuration for the SiteContent model.
    """
    list_display = ('page', 'section', 'title', 'updated_at')
    list_filter = ('page',)
    search_fields = ('title', 'content', 'section')
    list_editable = ('section', 'title',)
    ordering = ('page', 'section')
    save_on_top = True
    readonly_fields = ('updated_at',)