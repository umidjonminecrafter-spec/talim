from django.contrib import admin
from .models import (
    TaskBoards, TaskColumns, Task, TaskComments,
    TaskActivityLogs, TaskNotifications, TaskPermissions
)
# Register your models here.


# ==================== TASK ADMIN ====================
@admin.register(TaskBoards)
class TaskBoardsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_by', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'description')
    readonly_fields = ('created_at',)


@admin.register(TaskColumns)
class TaskColumnsAdmin(admin.ModelAdmin):
    list_display = ('id', 'board', 'name', 'position', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'board__name')
    readonly_fields = ('created_at',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'board', 'column', 'title', 'assigned_to', 'deadline', 'priority', 'status', 'created_by', 'created_at')
    list_filter = ('priority', 'status', 'deadline', 'created_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(TaskComments)
class TaskCommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'user', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('task__title', 'user__username', 'comment')
    readonly_fields = ('created_at',)


@admin.register(TaskActivityLogs)
class TaskActivityLogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'user', 'performed_by', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('task__title', 'user__username')
    readonly_fields = ('created_at',)


@admin.register(TaskNotifications)
class TaskNotificationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'user', 'notify_at', 'is_sent', 'created_at')
    list_filter = ('is_sent', 'notify_at', 'created_at')
    search_fields = ('task__title', 'user__username')
    readonly_fields = ('created_at',)


@admin.register(TaskPermissions)
class TaskPermissionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'user', 'can_edit', 'can_change_deadline', 'can_change_column', 'created_at')
    list_filter = ('can_edit', 'can_change_deadline', 'can_change_column', 'created_at')
    search_fields = ('task__title', 'user__username')
    readonly_fields = ('created_at',)

