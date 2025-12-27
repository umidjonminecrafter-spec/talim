from django.db import models
from core.models import BaseModel, Gender
from core.validators import uz_phone_validator
from accounts.models import User


class CRMSource(BaseModel):
    name = models.CharField(max_length=250)

class CRMPipelines(BaseModel):
    name = models.CharField(max_length=250)
    position = models.PositiveIntegerField()

class CRMLead(BaseModel):
    STATUS = (
        ('active', 'Active'),
        ('converted', 'Converted'),
        ('lost', 'Lost')
    )
    full_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=20, validators=[uz_phone_validator,], unique=True)
    gender = models.CharField(max_length=1,
                              choices=Gender.choices,
                              null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS, default='active')
    source = models.ForeignKey(CRMSource, on_delete=models.SET_NULL, null=True, related_name="source")
    pipline = models.ForeignKey(CRMPipelines, on_delete=models.SET_NULL, null=True, related_name="pipline")
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="assigned_to")
    expected_course = models.CharField(max_length=150, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    converted_student_id = models.PositiveIntegerField()

class CRMActivity(BaseModel):
    ACTIVITY_TYPE = (
        ('call', 'Call'),
        ('sms', 'SMS'),
        ('meeting', 'Meeting'),
    )

    lead = models.ForeignKey(CRMLead, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=10, choices=ACTIVITY_TYPE)
    result = models.CharField(max_length=250, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="created_by")

class CRMLeadsHistory(BaseModel):
    lead = models.ForeignKey(CRMLead, on_delete=models.CASCADE, related_name='lead')
    old_pipeline = models.ForeignKey(CRMPipelines, on_delete=models.SET_NULL, null=True, related_name='+')
    new_pipeline = models.ForeignKey(CRMPipelines, on_delete=models.SET_NULL, null=True, related_name="+")
    changed_by = models.ForeignKey(User, models.SET_NULL, null=True)
    changed_at = models.DateTimeField(auto_now_add=True)

class CRMLostReason(BaseModel):
    name = models.CharField(max_length=200)

class CRMLeadLost(BaseModel):
    lead = models.ForeignKey(CRMLead, on_delete=models.CASCADE, related_name="leads")
    reason = models.ForeignKey(CRMLostReason, on_delete=models.SET, null=True, related_name="reason")
    comment = models.TextField(blank=True)

class CRMLeadNotes(BaseModel):
    lead = models.ForeignKey(CRMLead, on_delete=models.CASCADE, related_name='notes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="note_user")
    note = models.TextField()
