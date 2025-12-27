from django.db import models
from core.models import BaseModel
# from academics.models.lesson import LessonTime
from accounts.models import Employee

class Room(BaseModel):
    name = models.CharField(max_length=250)
    capacity = models.PositiveIntegerField()

class Course(BaseModel):
    name = models.CharField(max_length=250)
    code = models.CharField(max_length=200, blank=True)
    monthly_price = models.DecimalField(max_digits=10, decimal_places=2)
    lesson = models.ForeignKey('LessonTime', on_delete=models.SET_NULL, null=True, related_name="Course_lesson")
    lesson_month = models.PositiveIntegerField()
    comment = models.TextField(blank=True)


class Group(BaseModel):

    STATUS = (
        ("active", "Active"),
        ("expried", "Expired"),
        ("archived", "Archived")
    )
    name = models.CharField(max_length=250)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, related_name="group_course")
    status = models.CharField(max_length=20, choices=STATUS, default="active")
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, related_name="group_room")
    start_date = models.DateField()
    end_date = models.DateField()


class GroupTeacher(BaseModel):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="group")
    teacher = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="teacher")
    start_date = models.DateField()
    end_date = models.DateField()
