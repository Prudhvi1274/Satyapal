# theme/views.py
from rest_framework import generics
from .models import ThemeSetting
from .serializers import ThemeSettingSerializer

class ThemeSettingDetail(generics.RetrieveAPIView):
    queryset = ThemeSetting.objects.all()
    serializer_class = ThemeSettingSerializer

    def get_object(self):
        # FIX: Ab yeh view sirf active theme ko hi uthayega.
        # Agar koi bhi active nahi hai, toh pehla theme uthayega (Fallback).
        return ThemeSetting.objects.filter(is_active=True).first() or ThemeSetting.objects.first()