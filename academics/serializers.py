from rest_framework import serializers
from .models import (
    Student, StudentGroup, StudentPricing, StudentBalances,
    StudentTarnsactions, LeaveReason, StudentGroupLeaves,
    StudentFreezes, StudentBalanceHistory, Attendence,
    Room, Course, Group, GroupTeacher,
    LessonTime, LessonSchedule, Exams, ExamResults,
    TeacherSalaryRules, TeacherSalaryPayments, TeacherSalaryCalculations
)


# ==================== STUDENT SERIALIZERS ====================
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class StudentGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGroup
        fields = '__all__'


class StudentPricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentPricing
        fields = '__all__'


class StudentBalancesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentBalances
        fields = '__all__'


class StudentTarnsactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentTarnsactions
        fields = '__all__'


class LeaveReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveReason
        fields = '__all__'


class StudentGroupLeavesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGroupLeaves
        fields = '__all__'


class StudentFreezesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentFreezes
        fields = '__all__'


class StudentBalanceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentBalanceHistory
        fields = '__all__'


class AttendenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendence
        fields = '__all__'


# ==================== GROUP SERIALIZERS ====================
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class GroupTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupTeacher
        fields = '__all__'


# ==================== LESSON SERIALIZERS ====================
class LessonTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonTime
        fields = '__all__'


class LessonScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonSchedule
        fields = '__all__'


class ExamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exams
        fields = '__all__'


class ExamResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamResults
        fields = '__all__'




# ==================== TEACHER SERIALIZERS ====================
class TeacherSalaryRulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherSalaryRules
        fields = '__all__'


class TeacherSalaryPaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherSalaryPayments
        fields = '__all__'


class TeacherSalaryCalculationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherSalaryCalculations
        fields = '__all__'