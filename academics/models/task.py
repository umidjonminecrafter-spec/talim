from django.db import models
from core.models import BaseModel, student_avatar_upload_path, exam_files_upload_path
from accounts.models import Employee

class TaskBoards(BaseModel):
    name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name="Tboard_created")

class TaskColumns(BaseModel):
    board = models.ForeignKey(TaskBoards, on_delete=models.CASCADE, related_name="TColumn_board")
    name = models.CharField(max_length=250)
    position = models.PositiveIntegerField(default=0)

class Task(BaseModel):
    PRIORITY = (
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
        ("urgent", "Urgent")
    )

    STATUS = (
        ("active", "Active"),
        ("completed", "Completed"),
        ("archived", "Archived")
    )

    board = models.ForeignKey(TaskBoards, on_delete=models.CASCADE, related_name="Task_board")
    column = models.ForeignKey(TaskColumns, on_delete=models.CASCADE, related_name="Task_column")
    title = models.TextField()
    description = models.TextField()
    assigned_to = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name="Task_assigned")
    created_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name="Task_created")
    deadline = models.DateTimeField()
    priority = models.CharField(max_length=15, choices=PRIORITY)
    status = models.CharField(max_length=15, choices=STATUS)
    updated_at = models.DateTimeField(auto_now_add=True)

class TaskComments(BaseModel):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="TComment_task")
    user = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="TComment_user")
    comment = models.TextField()

class TaskActivityLogs(BaseModel):
    ACTION = (
        ("create", "Create"),
        ("update", "Update"),
        ("delete", "Delete"),
        ("moved", "Moved"),
        ("completed", "Completed"),
        ("deadline_change", "Deadline change")
    )
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="TActLog_task")
    user = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name="TActLog_user")
    old_value = models.JSONField(null=True, blank=True)
    new_value = models.JSONField(null=True, blank=True)
    performed_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name="TActLog_performed")

class TaskNotifications(BaseModel):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="TNotifi_task")
    user = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="TNotifi_user")
    notify_at = models.DateTimeField()
    is_sent = models.BooleanField(default=False)

class TaskPermissions(BaseModel):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="TPerm_task")
    user = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="TPerm_user")
    can_edit = models.BooleanField(default=False)
    can_change_deadline = models.BooleanField(default=False)
    can_change_column = models.BooleanField(default=True)






















