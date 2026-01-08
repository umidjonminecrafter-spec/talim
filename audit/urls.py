from django.urls import path
from .views import AuditLogViewSet

urlpatterns = [
    # AuditLog URLs
    path('audit-logs/', AuditLogViewSet.as_view({'get': 'list', 'post': 'create'}), name='auditlog-list'),
    path('audit-logs/<int:pk>/', AuditLogViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='auditlog-detail'),
]