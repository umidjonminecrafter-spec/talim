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

class CRMSourceViewSet(ModelViewSet):
    queryset = CRMSource.objects.all()
    serializer_class = CRMSourceSerializer

class CRMPipelinesViewSet(ModelViewSet):
    queryset = CRMPipelines.objects.all()
    serializer_class = CRMPipelinesSerializer

class CRMLeadViewSet(ModelViewSet):
    queryset = CRMLead.objects.all()
    serializer_class = CRMLeadSerializer

class CRMActivityViewSet(ModelViewSet):
    queryset = CRMActivity.objects.all()
    serializer_class = CRMActivitySerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class CRMLeadsHistoryViewSet(ModelViewSet):
    queryset = CRMLeadsHistory.objects.all()
    serializer_class = CRMLeadsHistorySerializer

    def perform_create(self, serializer):
        serializer.save(changed_by=self.request.user)

class CRMLostReasonViewSet(ModelViewSet):
    queryset = CRMLostReason.objects.all()
    serializer_class = CRMLostReasonSerializer

class CRMLeadLostViewSet(ModelViewSet):
    queryset = CRMLeadLost.objects.all()
    serializer_class = CRMLeadLostSerializer


class CRMLeadNotesViewSet(ModelViewSet):
    queryset = CRMLeadNotes.objects.all()
    serializer_class = CRMLeadNotesSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
