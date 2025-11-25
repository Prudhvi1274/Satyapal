from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = BlogPost
        fields = ["id", "title", "slug", "short_description", "body", "image", "published", "created_at"]
