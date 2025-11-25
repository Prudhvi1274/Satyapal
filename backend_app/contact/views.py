from rest_framework import viewsets, mixins
from .models import ContactMessage
from .serializers import ContactSerializer

class ContactViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = ContactMessage.objects.all().order_by("-created_at")
    serializer_class = ContactSerializer
