from django.contrib import admin
from .models import (
    Student, StudentGroup, StudentPricing, StudentBalances,
    StudentTarnsactions, LeaveReason, StudentGroupLeaves,
    StudentFreezes, StudentBalanceHistory, Attendence,
    Room, Course, Group, GroupTeacher,
    LessonTime, LessonSchedule, Exams, ExamResults,
    TeacherSalaryRules, TeacherSalaryPayments, TeacherSalaryCalculations
)


# ==================== STUDENT ADMIN ====================
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone_number', 'phone_number2', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('full_name', 'phone_number', 'phone_number2', 'email', 'telegram_username')
    readonly_fields = ('created_at',)


@admin.register(StudentGroup)
class StudentGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'group', 'joined_at', 'left_at', 'end_date')
    list_filter = ('joined_at', 'left_at', 'end_date')
    search_fields = ('student__full_name', 'group__name')
    readonly_fields = ('created_at',)


@admin.register(StudentPricing)
class StudentPricingAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'price_override', 'start_date', 'end_date', 'created_by')
    list_filter = ('start_date', 'end_date', 'created_at')
    search_fields = ('student__full_name', 'course__name', 'reason')
    readonly_fields = ('created_at',)


@admin.register(StudentBalances)
class StudentBalancesAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'balance', 'updated_at')
    list_filter = ('updated_at',)
    search_fields = ('student__full_name',)
    readonly_fields = ('updated_at', 'created_at')


@admin.register(StudentTarnsactions)
class StudentTarnsactionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'transaction_type', 'amount', 'payment_type', 'transaction_date', 'accepted_by')
    list_filter = ('transaction_type', 'payment_type', 'transaction_date')
    search_fields = ('student__full_name', 'comment')
    readonly_fields = ('created_at',)


@admin.register(LeaveReason)
class LeaveReasonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name',)
    readonly_fields = ('created_at',)


@admin.register(StudentGroupLeaves)
class StudentGroupLeavesAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'group', 'leave_date', 'leave_reason', 'recalc_balance', 'refound_amount', 'created_by')
    list_filter = ('leave_date', 'recalc_balance', 'created_at')
    search_fields = ('student__full_name', 'group__name', 'comment')
    readonly_fields = ('created_at',)


@admin.register(StudentFreezes)
class StudentFreezesAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'group', 'freeze_start_date', 'freeze_end_date', 'recalc_balance', 'created_by')
    list_filter = ('freeze_start_date', 'freeze_end_date', 'recalc_balance')
    search_fields = ('student__full_name', 'group__name', 'reason')
    readonly_fields = ('created_at',)


@admin.register(StudentBalanceHistory)
class StudentBalanceHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'amount', 'base_price', 'applied_price', 'discount', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('student__full_name',)
    readonly_fields = ('created_at',)


@admin.register(Attendence)
class AttendenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_group', 'lesson_date', 'is_present', 'marked_by', 'created_at')
    list_filter = ('lesson_date', 'is_present', 'created_at')
    search_fields = ('student_group__student__full_name',)
    readonly_fields = ('created_at',)


# ==================== GROUP ADMIN ====================
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'capacity', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name',)
    readonly_fields = ('created_at',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'monthly_price', 'lesson', 'lesson_month', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'code')
    readonly_fields = ('created_at',)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'course', 'status', 'room', 'start_date', 'end_date', 'created_at')
    list_filter = ('status', 'start_date', 'end_date', 'created_at')
    search_fields = ('name', 'course__name', 'room__name')
    readonly_fields = ('created_at',)


@admin.register(GroupTeacher)
class GroupTeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'group', 'teacher', 'start_date', 'end_date', 'created_at')
    list_filter = ('start_date', 'end_date', 'created_at')
    search_fields = ('group__name', 'teacher__username')
    readonly_fields = ('created_at',)


# ==================== LESSON ADMIN ====================
@admin.register(LessonTime)
class LessonTimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'code')
    readonly_fields = ('created_at',)


@admin.register(LessonSchedule)
class LessonScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'group', 'day_type', 'start_time', 'end_time', 'created_at')
    list_filter = ('day_type', 'created_at')
    search_fields = ('group__name',)
    readonly_fields = ('created_at',)


@admin.register(Exams)
class ExamsAdmin(admin.ModelAdmin):
    list_display = ('id', 'group', 'title', 'exam_date', 'min_score', 'max_score', 'created_by', 'created_at')
    list_filter = ('exam_date', 'created_at')
    search_fields = ('title', 'group__name', 'description')
    readonly_fields = ('created_at',)


@admin.register(ExamResults)
class ExamResultsAdmin(admin.ModelAdmin):
    list_display = ('id', 'exam', 'student', 'score', 'created_by', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('exam__title', 'student__full_name', 'comment')
    readonly_fields = ('created_at',)


# ==================== TEACHER ADMIN ====================
@admin.register(TeacherSalaryRules)
class TeacherSalaryRulesAdmin(admin.ModelAdmin):
    list_display = ('id', 'teacher', 'percent_per_student', 'fixed_bonus', 'effective_from', 'effective_to', 'created_at')
    list_filter = ('effective_from', 'effective_to', 'created_at')
    search_fields = ('teacher__username',)
    readonly_fields = ('created_at',)


@admin.register(TeacherSalaryPayments)
class TeacherSalaryPaymentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'teacher', 'amount', 'payment_date', 'payment_type', 'created_at')
    list_filter = ('payment_type', 'payment_date', 'created_at')
    search_fields = ('teacher__username',)
    readonly_fields = ('created_at',)


@admin.register(TeacherSalaryCalculations)
class TeacherSalaryCalculationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'teacher', 'group', 'month', 'student_count', 'percent', 'total_amount', 'calculated_at', 'created_at')
    list_filter = ('month', 'calculated_at', 'created_at')
    search_fields = ('teacher__username', 'group__name')
    readonly_fields = ('created_at',)