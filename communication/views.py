from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema

from audit.models import AuditLog
from .models import SmsTemplates, SmsSchedules, SMSMessages, SmsProvider
from .serializers import (
    SmsTemplatesSerializer, SmsSchedulesSerializer,
    SMSMessagesSerializer, SmsProviderSerializer, SmsProviderListSerializer,
)


# ─── AuditLog helper ─────────────────────────────────────────────

def _log(entity_type, entity_id, action, old_data, new_data, user):
    try:
        employee = user.employee if hasattr(user, 'employee') else None
        AuditLog.objects.create(
            entity_type=entity_type,
            entity_id=entity_id,
            action=action,
            old_data=old_data,
            new_action=new_data,
            performed_by=employee,
            performed_by_role=employee.position if employee else '',
        )
    except Exception:
        pass


# ════════════════════════════════════════════════════════════════
#  SMS TEMPLATES
# ════════════════════════════════════════════════════════════════

@extend_schema(tags=["SmsTemplates - SMS shablonlar yaratish"])
class SmsTemplatesViewSet(ModelViewSet):
    queryset         = SmsTemplates.objects.all()
    serializer_class = SmsTemplatesSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        obj = serializer.save()
        _log('other', obj.id, 'create', None, {
            'action': 'SMS shablon yaratildi',
            'name':   obj.name,
        }, self.request.user)

    def perform_update(self, serializer):
        old = {'name': serializer.instance.name, 'is_active': serializer.instance.is_active}
        obj = serializer.save()
        _log('other', obj.id, 'update', old, {
            'name':      obj.name,
            'is_active': obj.is_active,
        }, self.request.user)

    def perform_destroy(self, instance):
        _log('other', instance.id, 'delete',
             {'name': instance.name}, None, self.request.user)
        instance.delete()


# ════════════════════════════════════════════════════════════════
#  SMS SCHEDULES
# ════════════════════════════════════════════════════════════════

@extend_schema(tags=["SmsSchedules - SMS larni rejalashtirish"])
class SmsSchedulesViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset           = SmsSchedules.objects.select_related('template', 'created_by').all()
    serializer_class   = SmsSchedulesSerializer
    filter_backends    = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields   = ['is_active', 'target_type']
    search_fields      = ['name']
    ordering_fields    = ['created_at', 'send_at', 'name']
    ordering           = ['-created_at']

    def perform_create(self, serializer):
        obj = serializer.save()
        _log('other', obj.id, 'create', None, {
            'action':      'SMS jadval yaratildi',
            'name':        obj.name,
            'target_type': obj.target_type,
            'send_at':     str(obj.send_at) if obj.send_at else None,
        }, self.request.user)

    def perform_update(self, serializer):
        old = {'name': serializer.instance.name, 'is_active': serializer.instance.is_active}
        obj = serializer.save()
        _log('other', obj.id, 'update', old, {
            'name':      obj.name,
            'is_active': obj.is_active,
        }, self.request.user)

    def perform_destroy(self, instance):
        _log('other', instance.id, 'delete',
             {'name': instance.name, 'target_type': instance.target_type},
             None, self.request.user)
        instance.delete()


# ════════════════════════════════════════════════════════════════
#  SMS PROVIDER
# ════════════════════════════════════════════════════════════════

@extend_schema(tags=["SmsProvider - SMS provayderlarni sozlash"])
class SmsProviderViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset           = SmsProvider.objects.select_related('created_by').all()
    serializer_class   = SmsProviderSerializer
    filter_backends    = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields   = ['is_active', 'provider']
    search_fields      = ['email', 'nickname']
    ordering_fields    = ['created_at', 'balance']
    ordering           = ['-created_at']

    def get_serializer_class(self):
        if self.action == 'list':
            return SmsProviderListSerializer
        return SmsProviderSerializer

    def perform_create(self, serializer):
        obj = serializer.save()
        _log('other', obj.id, 'create', None, {
            'action':   'SMS provayder qo\'shildi',
            'provider': obj.provider,
            'email':    obj.email,
        }, self.request.user)

    def perform_update(self, serializer):
        old = {'provider': serializer.instance.provider, 'is_active': serializer.instance.is_active}
        obj = serializer.save()
        _log('other', obj.id, 'update', old, {
            'provider':  obj.provider,
            'is_active': obj.is_active,
        }, self.request.user)

    def perform_destroy(self, instance):
        _log('other', instance.id, 'delete',
             {'provider': instance.provider, 'email': instance.email},
             None, self.request.user)
        instance.delete()


# ════════════════════════════════════════════════════════════════
#  SMS MESSAGES  (faqat o'qish uchun)
# ════════════════════════════════════════════════════════════════

@extend_schema(tags=["SMSMessages - SMS xabarlarni ko'rish"])
class SMSMessagesViewSet(ModelViewSet):
    queryset           = SMSMessages.objects.all().order_by('-created_at')
    serializer_class   = SMSMessagesSerializer
    permission_classes = [IsAuthenticated]
    # SMS xabarlar avtomatik yaratiladi — qo'lda AuditLog shart emas

