from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactAdmin(admin.ModelAdmin):
    # FIX: Added 'message' to list_display
    list_display = ("name", "email", "message", "created_at")
    search_fields = ("name", "email", "message")