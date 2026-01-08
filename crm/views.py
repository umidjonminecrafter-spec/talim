from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet
from .models import (
    CRMSource, CRMPipelines, CRMLead,
    CRMActivity, CRMLeadsHistory,
    CRMLostReason, CRMLeadLost, CRMLeadNotes
)
from .serializers import (
    CRMSourceSerializer, CRMPipelinesSerializer, CRMLeadSerializer,
    CRMActivitySerializer, CRMLeadsHistorySerializer,
    CRMLostReasonSerializer, CRMLeadLostSerializer, CRMLeadNotesSerializer
)

@extend_schema(tags=["CRMSource - Leadlar qayerdan kelyapti"])
class CRMSourceViewSet(ModelViewSet):
    queryset = CRMSource.objects.all()
    serializer_class = CRMSourceSerializer


@extend_schema(tags=["CRMPipelines - Lead varonkasini ko'rish"])
class CRMPipelinesViewSet(ModelViewSet):
    queryset = CRMPipelines.objects.all()
    serializer_class = CRMPipelinesSerializer


@extend_schema(tags=["CRMLead - Leadlarni ko'rish"])
class CRMLeadViewSet(ModelViewSet):
    queryset = CRMLead.objects.all()
    serializer_class = CRMLeadSerializer



@extend_schema(tags=["CRMActivity - Leadlar ustida bajarilgan barcha ishlarni ko'rsatish"])
class CRMActivityViewSet(ModelViewSet):
    queryset = CRMActivity.objects.all()
    serializer_class = CRMActivitySerializer


@extend_schema(tags=["CRMLeadsHistory - Lead ni butun tarixini ko'rsatish"])
class CRMLeadsHistoryViewSet(ModelViewSet):
    queryset = CRMLeadsHistory.objects.all()
    serializer_class = CRMLeadsHistorySerializer


@extend_schema(tags=["CRMLostReason - Leadlar ni ketib qolish qolish sabablari kiritish"])
class CRMLostReasonViewSet(ModelViewSet):
    queryset = CRMLostReason.objects.all()
    serializer_class = CRMLostReasonSerializer


@extend_schema(tags=["CRMLeadLost - Leadlarni ketib qolishlarini ko'rish"])
class CRMLeadLostViewSet(ModelViewSet):
    queryset = CRMLeadLost.objects.all()
    serializer_class = CRMLeadLostSerializer


@extend_schema(tags=["CRMLeadNotes - Lead ga yozilgan izohlar"])
class CRMLeadNotesViewSet(ModelViewSet):
    queryset = CRMLeadNotes.objects.all()
    serializer_class = CRMLeadNotesSerializer


