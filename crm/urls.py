from django.urls import path
from .views import (
    CRMSourceViewSet,
    CRMPipelinesViewSet,
    CRMLeadViewSet,
    CRMActivityViewSet,
    CRMLeadsHistoryViewSet,
    CRMLostReasonViewSet,
    CRMLeadLostViewSet,
    CRMLeadNotesViewSet
)

urlpatterns = [
    path('crm-sources/', CRMSourceViewSet.as_view({'get': 'list', 'post': 'create'}), name='crmsource-list'),
    path('crm-sources/<int:pk>/', CRMSourceViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'
    }), name='crmsource-detail'),


    path('crm-pipelines/', CRMPipelinesViewSet.as_view({'get': 'list', 'post': 'create'}), name='crmpipeline-list'),
    path('crm-pipelines/<int:pk>/', CRMPipelinesViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'
    }), name='crmpipeline-detail'),


    path('crm-leads/', CRMLeadViewSet.as_view({'get': 'list', 'post': 'create'}), name='crmlead-list'),
    path('crm-leads/<int:pk>/', CRMLeadViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'
    }), name='crmlead-detail'),


    path('crm-activities/', CRMActivityViewSet.as_view({'get': 'list', 'post': 'create'}), name='crmactivity-list'),
    path('crm-activities/<int:pk>/', CRMActivityViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'
    }), name='crmactivity-detail'),


    path('crm-leads-history/', CRMLeadsHistoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='crmleadshistory-list'),
    path('crm-leads-history/<int:pk>/', CRMLeadsHistoryViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'
    }), name='crmleadshistory-detail'),


    path('crm-lost-reasons/', CRMLostReasonViewSet.as_view({'get': 'list', 'post': 'create'}), name='crmlostreason-list'),
    path('crm-lost-reasons/<int:pk>/', CRMLostReasonViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'
    }), name='crmlostreason-detail'),


    path('crm-lead-lost/', CRMLeadLostViewSet.as_view({'get': 'list', 'post': 'create'}), name='crmleadlost-list'),
    path('crm-lead-lost/<int:pk>/', CRMLeadLostViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'
    }), name='crmleadlost-detail'),


    path('crm-lead-notes/', CRMLeadNotesViewSet.as_view({'get': 'list', 'post': 'create'}), name='crmleadnotes-list'),
    path('crm-lead-notes/<int:pk>/', CRMLeadNotesViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'
    }), name='crmleadnotes-detail'),
]
