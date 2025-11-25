from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import (
    SiteContent, Page,
    HomeContent, AboutContent, ServicesContent,
    ContactContent, CareersContent, ResourcesContent,
    CaseStudy, Resource, Service,
    FooterContent # <--- Task 3: FooterContent Imported
)

# 1. Page Admin
@admin.register(Page)
class PageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'slug', 'page_order')
    search_fields = ('title', 'slug')
    ordering = ('page_order',)
    
    # SEO Fields
    fieldsets = (
        (None, {'fields': ('title', 'slug')}),
        ('SEO Settings', {
            'fields': ('meta_title', 'meta_description', 'keywords'),
            'classes': ('collapse',),
        }),
    )

# 2. Base Content Admin (Logic for all pages)
class BaseContentAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('section_name', 'title', 'updated_at')
    search_fields = ('title', 'content', 'section_name')
    ordering = ('content_order',)
    save_on_top = True
    
    # FIX: section_name ko read-only banaya gaya hai.
    readonly_fields = ('page', 'section_name', 'section', 'updated_at')

    fieldsets = (
        ('Section Info', {
            # FIX: section_name ko yahan se hata diya gaya hai.
            'fields': ('title', 'image'),
            'description': 'Main content title and image for this section.'
        }),
        ('Content', {
            'fields': ('content',),
            'description': 'Main text content. HTML is allowed.'
        }),
        ('System Data (Do Not Edit)', {
            # FIX: section_name ko yahan read-only dikhaya jayega.
            'fields': ('page', 'section_name', 'section', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

# 3. Specific Page Admins (Inhein change karne ki zaroorat nahi, Base Admin inherit ho raha hai)
@admin.register(HomeContent)
class HomeContentAdmin(BaseContentAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(page='home')
    
    def save_model(self, request, obj, form, change):
        obj.page = 'home'
        super().save_model(request, obj, form, change)

@admin.register(AboutContent)
class AboutContentAdmin(BaseContentAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(page='about')
    
    def save_model(self, request, obj, form, change):
        obj.page = 'about'
        super().save_model(request, obj, form, change)

@admin.register(ServicesContent)
class ServicesContentAdmin(BaseContentAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(page='services')

    def save_model(self, request, obj, form, change):
        obj.page = 'services'
        super().save_model(request, obj, form, change)

@admin.register(ContactContent)
class ContactContentAdmin(BaseContentAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(page='contact')

    def save_model(self, request, obj, form, change):
        obj.page = 'contact'
        super().save_model(request, obj, form, change)

@admin.register(CareersContent)
class CareersContentAdmin(BaseContentAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(page='careers')

    def save_model(self, request, obj, form, change):
        obj.page = 'careers'
        super().save_model(request, obj, form, change)

@admin.register(ResourcesContent)
class ResourcesContentAdmin(BaseContentAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(page='resources')

    def save_model(self, request, obj, form, change):
        obj.page = 'resources'
        super().save_model(request, obj, form, change)

# <--- Task 3: NEW: Footer Content Admin Registration
@admin.register(FooterContent)
class FooterContentAdmin(BaseContentAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(page='footer').order_by('section_name') 

    def save_model(self, request, obj, form, change):
        obj.page = 'footer' # Ensure all saves go to the 'footer' page
        super().save_model(request, obj, form, change)
# NEW: Footer Content Admin Registration --->

# 4. Master Admin (Backup)
@admin.register(SiteContent)
class SiteContentAdmin(BaseContentAdmin):
    # Master Admin par hum section_name ko editable rakh sakte hain, but Proxy Admin par nahi.
    # Lekin simpler rahe isliye yahan bhi read-only rakhenge.
    list_display = ('page', 'section_name', 'title', 'updated_at')
    list_filter = ('page',)
    readonly_fields = ('section', 'updated_at') 
    
    fieldsets = (
        ('Content Details', {
            'fields': ('page', 'section_name', 'title', 'content', 'image'),
        }),
        ('Metadata', {
            'fields': ('section', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

# 5. Service, CaseStudy, Resource Registration
@admin.register(CaseStudy)
class CaseStudyAdmin(admin.ModelAdmin):
    list_display = ('title', 'client_name', 'created_at')
    search_fields = ('title', 'client_name')

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'created_at')
    list_filter = ('type',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'order')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('order',)