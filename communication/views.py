from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet
from .models import SmsTemplates, SmsSchedules, SMSMessages
from .serializers import (
    SmsTemplatesSerializer,
    SmsSchedulesSerializer,
    SMSMessagesSerializer
)

@extend_schema(tags=["SmsTemplates - sms templatelar yaratish"])
class SmsTemplatesViewSet(ModelViewSet):
    queryset = SmsTemplates.objects.all()
    serializer_class = SmsTemplatesSerializer


@extend_schema(tags=["SmsSchedules - Sms larni rejalash"])
class SmsSchedulesViewSet(ModelViewSet):
    queryset = SmsSchedules.objects.all()
    serializer_class = SmsSchedulesSerializer

@extend_schema(tags=["SMSMessages - Sms xabarlarni ko'rish"])
class SMSMessagesViewSet(ModelViewSet):
    queryset = SMSMessages.objects.all()
    serializer_class = SMSMessagesSerializer

