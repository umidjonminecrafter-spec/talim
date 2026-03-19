from django.urls import path
from .views import AuditLogViewSet
from . import views
urlpatterns = [
    # AuditLog URLs
    path('audit-logs/', AuditLogViewSet.as_view({'get': 'list', 'post': 'create'}), name='auditlog-list'),
    path('audit-logs/<int:pk>/', AuditLogViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='auditlog-detail'),
    # Davomat hisoboti
    path('reports/attendance/',
         views.attendance_report_v2,
         name='attendance-report'),

    # Batafsil davomat hisoboti (har bir talaba)
    path('reports/attendance/detailed/',
         views.detailed_attendance_report,
         name='detailed-attendance-report'),

    # Faol guruhlar ro'yxati (filtr uchun)
    path('reports/groups/',
         views.active_groups_list,
         name='active-groups-list'),
]