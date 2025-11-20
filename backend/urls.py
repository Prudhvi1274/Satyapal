# C:\Users\Ankur Sati\OneDrive\Desktop\XpertAI_Website\backend\urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from cms.views import SiteContentViewSet
from blog.views import BlogPostViewSet
from leads.views import LeadViewSet
from contact.views import ContactViewSet

router = DefaultRouter()
router.register(r"sitecontent", SiteContentViewSet, basename="sitecontent")
router.register(r"blogs", BlogPostViewSet, basename="blog")
router.register(r"leads", LeadViewSet, basename="lead")
router.register(r"contact", ContactViewSet, basename="contact")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
