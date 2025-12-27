from django.db import models
from core.models import BaseModel, exam_files_upload_path
# from academics.models.student import Student
# from academics.models.group import Group
from accounts.models import Employee

class LessonTime(BaseModel):
    name = models.CharField(max_length=250)
    code = models.CharField(max_length=200, blank=True)
class LessonSchedule(BaseModel):

    DAY_TYPE = (
        ("odd", "Odd days"),
        ("even", "Even days"),
        ("every", "EveryDaye")
    )
    group = models.ForeignKey('Group', on_delete=models.CASCADE, related_name="lesson_group")
    day_type = models.CharField(max_length=20, choices=DAY_TYPE)
    start_time = models.TimeField()
    end_time = models.TimeField()


class Exams(BaseModel):
    group = models.ForeignKey('Group', on_delete=models.CASCADE, related_name="exams_group")
    title = models.CharField(max_length=250)
    exam_date = models.DateField()
    min_score = models.DecimalField(max_digits=12, decimal_places=2)
    max_score = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to=exam_files_upload_path, null=True, blank=True)
    created_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name="exam_created")

class ExamResults(BaseModel):
    exam = models.ForeignKey(Exams, on_delete=models.SET_NULL, null=True, related_name="exam")
    student = models.ForeignKey('Student', on_delete=models.SET_NULL, null=True, related_name="exam_res_student")
    score = models.DecimalField(max_digits=12, decimal_places=2)
    comment = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name="exam_res_created")
