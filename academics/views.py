from rest_framework import viewsets
from drf_spectacular.utils import extend_schema
from .models import (
    Student, StudentGroup, StudentPricing, StudentBalances,
    StudentTarnsactions, LeaveReason, StudentGroupLeaves,
    StudentFreezes, StudentBalanceHistory, Attendence,
    Room, Course, Group, GroupTeacher,
    LessonTime, LessonSchedule, Exams, ExamResults,
    TaskBoards, TaskColumns, Task, TaskComments,
    TaskActivityLogs, TaskNotifications, TaskPermissions,
    TeacherSalaryRules, TeacherSalaryPayments, TeacherSalaryCalculations
)
from .serializers import (
    StudentSerializer, StudentGroupSerializer, StudentPricingSerializer,
    StudentBalancesSerializer, StudentTarnsactionsSerializer, LeaveReasonSerializer,
    StudentGroupLeavesSerializer, StudentFreezesSerializer, StudentBalanceHistorySerializer,
    AttendenceSerializer, RoomSerializer, CourseSerializer, GroupSerializer,
    GroupTeacherSerializer, LessonTimeSerializer, LessonScheduleSerializer,
    ExamsSerializer, ExamResultsSerializer, TaskBoardsSerializer,
    TaskColumnsSerializer, TaskSerializer, TaskCommentsSerializer,
    TaskActivityLogsSerializer, TaskNotificationsSerializer, TaskPermissionsSerializer,
    TeacherSalaryRulesSerializer, TeacherSalaryPaymentsSerializer, TeacherSalaryCalculationsSerializer
)


# ==================== STUDENT VIEWSETS ====================
@extend_schema(tags=["Students"])
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentGroupViewSet(viewsets.ModelViewSet):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupSerializer


class StudentPricingViewSet(viewsets.ModelViewSet):
    queryset = StudentPricing.objects.all()
    serializer_class = StudentPricingSerializer


class StudentBalancesViewSet(viewsets.ModelViewSet):
    queryset = StudentBalances.objects.all()
    serializer_class = StudentBalancesSerializer


class StudentTarnsactionsViewSet(viewsets.ModelViewSet):
    queryset = StudentTarnsactions.objects.all()
    serializer_class = StudentTarnsactionsSerializer


class LeaveReasonViewSet(viewsets.ModelViewSet):
    queryset = LeaveReason.objects.all()
    serializer_class = LeaveReasonSerializer


class StudentGroupLeavesViewSet(viewsets.ModelViewSet):
    queryset = StudentGroupLeaves.objects.all()
    serializer_class = StudentGroupLeavesSerializer


class StudentFreezesViewSet(viewsets.ModelViewSet):
    queryset = StudentFreezes.objects.all()
    serializer_class = StudentFreezesSerializer


class StudentBalanceHistoryViewSet(viewsets.ModelViewSet):
    queryset = StudentBalanceHistory.objects.all()
    serializer_class = StudentBalanceHistorySerializer


class AttendenceViewSet(viewsets.ModelViewSet):
    queryset = Attendence.objects.all()
    serializer_class = AttendenceSerializer


# ==================== GROUP VIEWSETS ====================
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupTeacherViewSet(viewsets.ModelViewSet):
    queryset = GroupTeacher.objects.all()
    serializer_class = GroupTeacherSerializer


# ==================== LESSON VIEWSETS ====================
class LessonTimeViewSet(viewsets.ModelViewSet):
    queryset = LessonTime.objects.all()
    serializer_class = LessonTimeSerializer


class LessonScheduleViewSet(viewsets.ModelViewSet):
    queryset = LessonSchedule.objects.all()
    serializer_class = LessonScheduleSerializer


class ExamsViewSet(viewsets.ModelViewSet):
    queryset = Exams.objects.all()
    serializer_class = ExamsSerializer


class ExamResultsViewSet(viewsets.ModelViewSet):
    queryset = ExamResults.objects.all()
    serializer_class = ExamResultsSerializer


# ==================== TASK VIEWSETS ====================
class TaskBoardsViewSet(viewsets.ModelViewSet):
    queryset = TaskBoards.objects.all()
    serializer_class = TaskBoardsSerializer


class TaskColumnsViewSet(viewsets.ModelViewSet):
    queryset = TaskColumns.objects.all()
    serializer_class = TaskColumnsSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskCommentsViewSet(viewsets.ModelViewSet):
    queryset = TaskComments.objects.all()
    serializer_class = TaskCommentsSerializer


class TaskActivityLogsViewSet(viewsets.ModelViewSet):
    queryset = TaskActivityLogs.objects.all()
    serializer_class = TaskActivityLogsSerializer


class TaskNotificationsViewSet(viewsets.ModelViewSet):
    queryset = TaskNotifications.objects.all()
    serializer_class = TaskNotificationsSerializer


class TaskPermissionsViewSet(viewsets.ModelViewSet):
    queryset = TaskPermissions.objects.all()
    serializer_class = TaskPermissionsSerializer


# ==================== TEACHER VIEWSETS ====================
class TeacherSalaryRulesViewSet(viewsets.ModelViewSet):
    queryset = TeacherSalaryRules.objects.all()
    serializer_class = TeacherSalaryRulesSerializer


class TeacherSalaryPaymentsViewSet(viewsets.ModelViewSet):
    queryset = TeacherSalaryPayments.objects.all()
    serializer_class = TeacherSalaryPaymentsSerializer


class TeacherSalaryCalculationsViewSet(viewsets.ModelViewSet):
    queryset = TeacherSalaryCalculations.objects.all()
    serializer_class = TeacherSalaryCalculationsSerializer