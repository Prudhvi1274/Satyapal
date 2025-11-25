from django.contrib import admin
from .models import Lead, ChatbotLead, WebsiteLead, NewsletterSubscriber

@admin.register(ChatbotLead)
class ChatbotLeadAdmin(admin.ModelAdmin):
    # UPDATED list_display: message and service added
    list_display = ("name", "email", "phone", "service", "message", "created_at") 
    search_fields = ("name", "email", "service", "message")
    list_filter = ("service",)

@admin.register(WebsiteLead)
class WebsiteLeadAdmin(admin.ModelAdmin):
    # UPDATED list_display: service and message added
    list_display = ("name", "company", "email", "phone", "service", "message", "created_at") 
    search_fields = ("name", "email", "company", "service", "message")

@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    search_fields = ('email',)