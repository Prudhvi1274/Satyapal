from rest_framework import viewsets
from rest_framework import generics
from .models import BlogPost, BlogCategory
from .serializers import BlogPostSerializer
from rest_framework import serializers # Need to import standard serializer

# --- 1. NEW: CATEGORY SERIALIZER ---
class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ['name', 'slug']

# --- 2. NEW: CATEGORY VIEWSET (To fetch list of categories) ---
class BlogCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogCategory.objects.all().order_by('name')
    serializer_class = BlogCategorySerializer


# --- 3. UPDATED: BLOG POST VIEWSET (For filtering) ---
class BlogPostViewSet(viewsets.ModelViewSet):
    # queryset property will be replaced by get_queryset
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        # Base queryset to fetch all published blogs, ordered by date
        queryset = BlogPost.objects.filter(published=True).order_by("-created_at")
        
        # FIX: Implement filtering based on URL query parameter
        category_slug = self.request.query_params.get('category')
        
        if category_slug:
            if category_slug == 'all':
                # 'all' par koi filter nahi lagega
                return queryset
            else:
                # Filter blogs where BlogCategory's slug matches the URL slug
                queryset = queryset.filter(category__slug=category_slug)
        
        return queryset