# theme/admin.py

from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import ThemeSetting, ChatbotFlowStep # <--- NEW Import
from django.core.exceptions import ObjectDoesNotExist

@admin.register(ThemeSetting)
class ThemeAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'is_active', 
        'light_primary_color', 
        'light_secondary_color'
    )
    # is_active ko list page se hi edit kar sakte hain
    list_editable = ('is_active',) 
    search_fields = ('name',)

    # --- ENFORCE SINGLE ACTIVE THEME LOGIC ---
    def save_model(self, request, obj, form, change):
        if obj.is_active:
            # CRITICAL: Agar yeh theme active ho raha hai, toh baaki sab ko inactive kar do
            ThemeSetting.objects.exclude(pk=obj.pk).update(is_active=False)
        
        # Fallback logic to ensure at least one theme is active (simplified)
        if not obj.is_active and ThemeSetting.objects.filter(is_active=True).count() == 0 and ThemeSetting.objects.count() > 0:
             try:
                 first_theme = ThemeSetting.objects.first()
                 if first_theme and not first_theme.is_active:
                    first_theme.is_active = True
                    first_theme.save()
             except Exception:
                 pass 
        
        super().save_model(request, obj, form, change)

# <--- NEW ADMIN FOR CHATBOT FLOW (Task 1, 2)
@admin.register(ChatbotFlowStep)
class ChatbotFlowStepAdmin(SortableAdminMixin, admin.ModelAdmin):
    # SortableAdminMixin allows drag-and-drop ordering (using step_order)
    list_display = ('step_order', 'question_text', 'field_to_save', 'is_required')
    list_editable = ('question_text', 'field_to_save', 'is_required')
    ordering = ('step_order',)
    search_fields = ('question_text', 'field_to_save')
# NEW ADMIN FOR CHATBOT FLOW --->