from django.db import models

class ThemeSettings(models.Model):
    primary_color = models.CharField(max_length=7, default='#FFFFFF')
    secondary_color = models.CharField(max_length=7, default='#000000')
    font = models.CharField(max_length=100, default='Arial')

    def __str__(self):
        return "Theme Settings"

    class Meta:
        verbose_name_plural = "Theme Settings"

class StructureSettings(models.Model):
    show_hero_section = models.BooleanField(default=True)
    show_features_section = models.BooleanField(default=True)
    show_about_section = models.BooleanField(default=True)
    show_services_section = models.BooleanField(default=True)
    show_contact_section = models.BooleanField(default=True)

    def __str__(self):
        return "Structure Settings"

    class Meta:
        verbose_name_plural = "Structure Settings"
