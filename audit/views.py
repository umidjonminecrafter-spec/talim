from django.shortcuts import render
from drf_spectacular.utils import extend_schema

# Create your views here.
from rest_framework import viewsets
from .models import AuditLog
from .serializers import AuditLogSerializer

@extend_schema(tags=["AuditLog - Barcha bajarilgan ishlarni saqlab boradi "])
class AuditLogViewSet(viewsets.ModelViewSet):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer