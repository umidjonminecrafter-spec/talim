from rest_framework.routers import DefaultRouter
from .views import (
    CRMSourceViewSet, CRMPipelinesViewSet, CRMLeadViewSet,
    CRMActivityViewSet, CRMLeadsHistoryViewSet,
    CRMLostReasonViewSet, CRMLeadLostViewSet, CRMLeadNotesViewSet
)

router = DefaultRouter()
router.register("sources", CRMSourceViewSet)
router.register("pipelines", CRMPipelinesViewSet)
router.register("leads", CRMLeadViewSet)
router.register("activities", CRMActivityViewSet)
router.register("leads-history", CRMLeadsHistoryViewSet)
router.register("lost-reasons", CRMLostReasonViewSet)
router.register("lead-lost", CRMLeadLostViewSet)
router.register("lead-notes", CRMLeadNotesViewSet)

urlpatterns = router.urls
