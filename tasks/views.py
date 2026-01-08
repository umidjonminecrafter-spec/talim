from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from .models import (
TaskBoards, TaskColumns, Task, TaskComments,
    TaskActivityLogs, TaskNotifications, TaskPermissions,
)

from .serializers import (
TaskBoardsSerializer,
    TaskColumnsSerializer, TaskSerializer, TaskCommentsSerializer,
    TaskActivityLogsSerializer, TaskNotificationsSerializer, TaskPermissionsSerializer,
)

# ==================== TASK VIEWSETS ====================
@extend_schema(tags=["TaskBoards - Vazifalar doskasini ko'rish "])
class TaskBoardsViewSet(viewsets.ModelViewSet):
    queryset = TaskBoards.objects.all()
    serializer_class = TaskBoardsSerializer

@extend_schema(tags=["TaskColumns - Vazifalar ustunini ko'rish "])
class TaskColumnsViewSet(viewsets.ModelViewSet):
    queryset = TaskColumns.objects.all()
    serializer_class = TaskColumnsSerializer

@extend_schema(tags=["Task - Vazifalarni ko'rish "])
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

@extend_schema(tags=["TaskComments - Vazifalarga yozilgan izohlarni ko'rish "])
class TaskCommentsViewSet(viewsets.ModelViewSet):
    queryset = TaskComments.objects.all()
    serializer_class = TaskCommentsSerializer

@extend_schema(tags=["TaskActivityLogs - Vazifa ustida bajarilgan ishlarni ko'rish "])
class TaskActivityLogsViewSet(viewsets.ModelViewSet):
    queryset = TaskActivityLogs.objects.all()
    serializer_class = TaskActivityLogsSerializer

@extend_schema(tags=["TaskNotifications - Vazifa eslatmalarni ko'rish "])
class TaskNotificationsViewSet(viewsets.ModelViewSet):
    queryset = TaskNotifications.objects.all()
    serializer_class = TaskNotificationsSerializer

@extend_schema(tags=["TaskPermissions - Vazifaga berilgan ruxsatlarni ko'rish "])
class TaskPermissionsViewSet(viewsets.ModelViewSet):
    queryset = TaskPermissions.objects.all()
    serializer_class = TaskPermissionsSerializer
