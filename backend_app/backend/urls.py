# backend/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

# Existing imports
from cms.views import SiteContentViewSet, home_page_content, CaseStudyViewSet, ResourceViewSet, ServiceViewSet, PageViewSet 
# --- CRITICAL FIX: Only 'chat_flow_handler' is imported ---
from blog.views import BlogPostViewSet
from leads.views import LeadViewSet, NewsletterSubscriberViewSet, chat_flow_handler
from contact.views import ContactViewSet
from careers.views import JobOpeningViewSet, JobApplicationViewSet

# Router Setup
router = DefaultRouter()
# ... (router registration remains the same)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    # --- CRITICAL FIX: Path uses the new handler ---
    path("api/chatbot-flow/", chat_flow_handler),
    path("api/", include("theme.urls")),
    path("api/home-page-content/", home_page_content),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)