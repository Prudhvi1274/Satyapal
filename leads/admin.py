from django.contrib import admin
from .models import Lead, ChatbotLead, WebsiteLead

@admin.register(ChatbotLead)
class ChatbotLeadAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "service", "created_at")
    search_fields = ("name", "email", "service")
    list_filter = ("service",)

@admin.register(WebsiteLead)
class WebsiteLeadAdmin(admin.ModelAdmin):
    list_display = ("name", "company", "email", "phone", "created_at")
    search_fields = ("name", "email", "company")
