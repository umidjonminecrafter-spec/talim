from rest_framework import serializers
from .models import (
TaskBoards, TaskColumns, Task, TaskComments,
    TaskActivityLogs, TaskNotifications, TaskPermissions,
)

# ==================== TASK SERIALIZERS ====================
class TaskBoardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskBoards
        fields = '__all__'


class TaskColumnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskColumns
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TaskCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskComments
        fields = '__all__'


class TaskActivityLogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskActivityLogs
        fields = '__all__'


class TaskNotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskNotifications
        fields = '__all__'


class TaskPermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskPermissions
        fields = '__all__'
