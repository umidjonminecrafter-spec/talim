from django.db import models
from core.models import BaseModel
from accounts.models import Employee

class AuditEntityType(models.TextChoices):
    LEAD = "lead", "Lead"
    STUDENT = "student", "Student"
    PAYMENT = "payment", "Payment"
    GROUP = "group", "Group"
    USER = "user", "User"
    OTHER = "other", "Other"


class AuditAction(models.TextChoices):
    CREATE = "create", "Create"
    UPDATE = "update", "Update"
    DELETE = "delete", "Delete"


class AuditLog(BaseModel):
    entity_type = models.CharField(max_length=30, choices=AuditEntityType.choices)
    entity_id = models.UUIDField(help_text="O'zgartilgan entity UUID si")
    action = models.CharField(max_length=20, choices=AuditAction.choices)
    old_data = models.JSONField(
        null=True, blank=True
    )
    new_action = models.JSONField(null=True, blank=True)
    performed_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name="performed_by")
    performed_by_role = models.CharField(max_length=50)

