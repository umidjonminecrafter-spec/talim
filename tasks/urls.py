from .views import (
TaskBoardsViewSet,
    TaskColumnsViewSet, TaskViewSet, TaskCommentsViewSet,
    TaskActivityLogsViewSet, TaskNotificationsViewSet, TaskPermissionsViewSet,
)
from django.urls import path


urlpatterns = [
# ==================== TASK URLs ====================
path('task-boards/', TaskBoardsViewSet.as_view({'get': 'list', 'post': 'create'}), name='taskboards-list'),
path('task-boards/<int:pk>/', TaskBoardsViewSet.as_view(
    {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
     name='taskboards-detail'),

path('task-columns/', TaskColumnsViewSet.as_view({'get': 'list', 'post': 'create'}), name='taskcolumns-list'),
path('task-columns/<int:pk>/', TaskColumnsViewSet.as_view(
    {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
     name='taskcolumns-detail'),

path('tasks/', TaskViewSet.as_view({'get': 'list', 'post': 'create'}), name='task-list'),
path('tasks/<int:pk>/',
     TaskViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
     name='task-detail'),

path('task-comments/', TaskCommentsViewSet.as_view({'get': 'list', 'post': 'create'}), name='taskcomments-list'),
path('task-comments/<int:pk>/', TaskCommentsViewSet.as_view(
    {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
     name='taskcomments-detail'),

path('task-activity-logs/', TaskActivityLogsViewSet.as_view({'get': 'list', 'post': 'create'}),
     name='taskactivitylogs-list'),
path('task-activity-logs/<int:pk>/', TaskActivityLogsViewSet.as_view(
    {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
     name='taskactivitylogs-detail'),

path('task-notifications/', TaskNotificationsViewSet.as_view({'get': 'list', 'post': 'create'}),
     name='tasknotifications-list'),
path('task-notifications/<int:pk>/', TaskNotificationsViewSet.as_view(
    {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
     name='tasknotifications-detail'),

path('task-permissions/', TaskPermissionsViewSet.as_view({'get': 'list', 'post': 'create'}),
     name='taskpermissions-list'),
path('task-permissions/<int:pk>/', TaskPermissionsViewSet.as_view(
    {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
     name='taskpermissions-detail')
]
