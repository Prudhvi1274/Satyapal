from django.db import models

class Theme(models.Model):
    primary_color = models.CharField(max_length=7, default='#000000')
    secondary_color = models.CharField(max_length=7, default='#ffffff')
    font_family = models.CharField(max_length=50, default='Arial')

    def __str__(self):
        return "Site Theme"

class HomePageStructure(models.Model):
    SECTION_CHOICES = [
        ('features', 'Features'),
        ('about', 'About Us'),
        ('services', 'Services'),
        ('contact', 'Contact Us'),
    ]
    section_name = models.CharField(max_length=50, choices=SECTION_CHOICES, unique=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.get_section_name_display()} - Order: {self.order}"