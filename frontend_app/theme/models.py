# theme/models.py

from django.db import models
# from colorfield.fields import ColorField # Assuming ColorField is not needed or handled elsewhere

class ThemeSetting(models.Model):
    name = models.CharField(max_length=100, default="Default Theme")
    
    # --- NEW ACTIVE FIELD ---
    is_active = models.BooleanField(
        default=True, 
        help_text="Set to True to make this theme live on the website. Only one theme can be active."
    )
    
    # --- EXISTING FIELDS ---
    logo = models.ImageField(upload_to='site_config/', blank=True, null=True, help_text="Upload a transparent PNG logo for Header & Footer")
    light_primary_color = models.CharField(max_length=7, default='#10B981')
    light_secondary_color = models.CharField(max_length=7, default='#F59E0B')
    light_accent_color = models.CharField(max_length=7, default='#059669')
    light_background_color = models.CharField(max_length=7, default='#FFFFFF')
    light_text_color = models.CharField(max_length=7, default='#1F2937')
    dark_primary_color = models.CharField(max_length=7, default='#34D399')
    dark_secondary_color = models.CharField(max_length=7, default='#FBBF24')
    dark_accent_color = models.CharField(max_length=7, default='#10B981')
    dark_background_color = models.CharField(max_length=7, default='#111827')
    dark_text_color = models.CharField(max_length=7, default='#F3F4F6')

    # --- NEW DYNAMIC FIELDS (Footer & Chatbot) ---
    chatbot_welcome_message = models.TextField(
        default="👋 Hi! I’m XpertAI Assistant. How can I help you today?",
        help_text="Initial message shown by the chatbot."
    )
    contact_phone = models.CharField(max_length=20, default="+91 98765 43210", help_text="Phone number for Header/Footer")
    contact_email = models.EmailField(default="hello@xpertai.global", help_text="Email address for Header/Footer")
    
    # Social Media Links
    facebook_url = models.URLField(blank=True, help_text="Facebook URL")
    twitter_url = models.URLField(blank=True, help_text="Twitter/X URL")
    linkedin_url = models.URLField(blank=True, help_text="LinkedIn URL")
    instagram_url = models.URLField(blank=True, help_text="Instagram URL")

    def __str__(self):
        # Admin list mein active status dikhane ke liye update kiya
        return f"{self.name} {'(ACTIVE)' if self.is_active else ''}"

    class Meta:
        verbose_name_plural = "Theme Settings"


# <--- NEW MODEL FOR CHATBOT FLOW STEP (Task 1, 2, 3)
class ChatbotFlowStep(models.Model):
    FIELD_CHOICES = [
        ('name', 'Applicant Name'),
        ('email', 'Email Address'),
        ('phone', 'Phone Number'),
        ('service', 'Service Interest'),
        ('message', 'Message/Final Query'),
    ]

    question_text = models.CharField(max_length=255, help_text="The question the bot asks (e.g., 'What is your name?').")
    # Yeh field Lead model mein data store karega (Task 3)
    field_to_save = models.CharField(max_length=50, choices=FIELD_CHOICES, unique=True, 
                                     help_text="The Lead field this question's answer should populate.")
    step_order = models.PositiveIntegerField(default=0, help_text="Order in which questions are asked.")
    
    is_required = models.BooleanField(default=True)

    class Meta:
        ordering = ['step_order']
        verbose_name = "Chatbot Flow Step"
        verbose_name_plural = "Chatbot Flow Steps"

    def __str__(self):
        return f"Step {self.step_order}: {self.question_text[:40]}..."
# NEW MODEL FOR CHATBOT FLOW STEP --->