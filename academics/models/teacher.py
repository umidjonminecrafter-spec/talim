from django.db import models
from core.models import BaseModel, student_avatar_upload_path, exam_files_upload_path
from accounts.models import Employee
# from from academics.models.group import Group

class TeacherSalaryRules(BaseModel):
    teacher = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name="TSalRul_teacher")
    percent_per_student = models.DecimalField(max_digits=12, decimal_places=2)
    fixed_bonus = models.DecimalField(max_digits=12, decimal_places=2)
    effective_from = models.DateField()
    effective_to = models.DateField()

class TeacherSalaryPayments(BaseModel):
    PAYMENTTYPE = (
        ("cash", "Naqt Pul"),
        ("card", "Plastik karta"),
        ("check", "Bankdan o'tkazma")
    )
    teacher = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="TSalPay_teacher")
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_date = models.DateField()
    payment_type = models.CharField(max_length=20, choices=PAYMENTTYPE)

class TeacherSalaryCalculations(BaseModel):
    teacher = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="TSalCal_teacher")
    group = models.ForeignKey('Group', on_delete=models.CASCADE, related_name="TSalCal_group")
    month = models.CharField(max_length=250)
    student_count = models.PositiveIntegerField()
    percent = models.DecimalField(max_digits=6, decimal_places=2)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    calculated_at = models.DateField()
