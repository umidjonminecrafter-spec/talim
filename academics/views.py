from rest_framework import viewsets

from drf_spectacular.utils import extend_schema

from .models import (
    Student, StudentGroup, StudentPricing, StudentBalances,
    StudentTarnsactions, LeaveReason, StudentGroupLeaves,
    StudentFreezes, StudentBalanceHistory, Attendence,
    Room, Course, Group, GroupTeacher,
    LessonTime, LessonSchedule, Exams, ExamResults,
    TeacherSalaryRules, TeacherSalaryPayments, TeacherSalaryCalculations
)
from .serializers import (
    StudentSerializer, StudentGroupSerializer, StudentPricingSerializer,
    StudentBalancesSerializer, StudentTarnsactionsSerializer, LeaveReasonSerializer,
    StudentGroupLeavesSerializer, StudentFreezesSerializer, StudentBalanceHistorySerializer,
    AttendenceSerializer, RoomSerializer, CourseSerializer, GroupSerializer,
    GroupTeacherSerializer, LessonTimeSerializer, LessonScheduleSerializer,
    ExamsSerializer, ExamResultsSerializer,
    TeacherSalaryRulesSerializer, TeacherSalaryPaymentsSerializer, TeacherSalaryCalculationsSerializer
)


# ==================== STUDENT VIEWSETS ====================
@extend_schema(tags=["Students - Studentlar "])
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

@extend_schema(tags=["StudentGroup - Student va Guruh bog'langan jadval "])
class StudentGroupViewSet(viewsets.ModelViewSet):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupSerializer

@extend_schema(tags=["StudentPricing - Studentga narx belgilash "])
class StudentPricingViewSet(viewsets.ModelViewSet):
    queryset = StudentPricing.objects.all()
    serializer_class = StudentPricingSerializer

@extend_schema(tags=["StudentBalances - Studentning balansini ko'rish"])
class StudentBalancesViewSet(viewsets.ModelViewSet):
    queryset = StudentBalances.objects.all()
    serializer_class = StudentBalancesSerializer

@extend_schema(tags=["StudentTarnsactions - Student to'lovlarni tarixi"])
class StudentTarnsactionsViewSet(viewsets.ModelViewSet):
    queryset = StudentTarnsactions.objects.all()
    serializer_class = StudentTarnsactionsSerializer

@extend_schema(tags=["LeaveReason - Studentlarning chiqib ketish sabablari"])
class LeaveReasonViewSet(viewsets.ModelViewSet):
    queryset = LeaveReason.objects.all()
    serializer_class = LeaveReasonSerializer

@extend_schema(tags=["StudentGroupLeaves - Studentni guruhdan chiqib ketish "])
class StudentGroupLeavesViewSet(viewsets.ModelViewSet):
    queryset = StudentGroupLeaves.objects.all()
    serializer_class = StudentGroupLeavesSerializer

@extend_schema(tags=["StudentFreezes - Studentdarsni muzlatish"])
class StudentFreezesViewSet(viewsets.ModelViewSet):
    queryset = StudentFreezes.objects.all()
    serializer_class = StudentFreezesSerializer

@extend_schema(tags=["StudentBalanceHistory - Student balansi tarixi"])
class StudentBalanceHistoryViewSet(viewsets.ModelViewSet):
    queryset = StudentBalanceHistory.objects.all()
    serializer_class = StudentBalanceHistorySerializer

@extend_schema(tags=["Attendence - Yo'qlama"])
class AttendenceViewSet(viewsets.ModelViewSet):
    queryset = Attendence.objects.all()
    serializer_class = AttendenceSerializer


# ==================== GROUP VIEWSETS ====================
@extend_schema(tags=["Room - Xona"])
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

@extend_schema(tags=["Course - Kurslar"])
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

@extend_schema(tags=["Group - Guruh "])
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

@extend_schema(tags=["GroupTeacher - Guruhlarni o'qituvchilarga bog'lash "])
class GroupTeacherViewSet(viewsets.ModelViewSet):
    queryset = GroupTeacher.objects.all()
    serializer_class = GroupTeacherSerializer


# ==================== LESSON VIEWSETS ====================
@extend_schema(tags=["LessonTime - Dars vaqtlari "])
class LessonTimeViewSet(viewsets.ModelViewSet):
    queryset = LessonTime.objects.all()
    serializer_class = LessonTimeSerializer

@extend_schema(tags=["LessonSchedule - Dars jadvali ro'yxati "])
class LessonScheduleViewSet(viewsets.ModelViewSet):
    queryset = LessonSchedule.objects.all()
    serializer_class = LessonScheduleSerializer

@extend_schema(tags=["ExamsView - Imtihonlar jadvlai "])
class ExamsViewSet(viewsets.ModelViewSet):
    queryset = Exams.objects.all()
    serializer_class = ExamsSerializer

@extend_schema(tags=["ExamResults - Imtihonlar natijalari "])
class ExamResultsViewSet(viewsets.ModelViewSet):
    queryset = ExamResults.objects.all()
    serializer_class = ExamResultsSerializer



# ==================== TEACHER VIEWSETS ====================
@extend_schema(tags=["TeacherSalaryRules - O'qituvchi oylik qoidalari "])
class TeacherSalaryRulesViewSet(viewsets.ModelViewSet):
    queryset = TeacherSalaryRules.objects.all()
    serializer_class = TeacherSalaryRulesSerializer

@extend_schema(tags=["TeacherSalaryPayments - O'qituvchilarga oylik berish"])
class TeacherSalaryPaymentsViewSet(viewsets.ModelViewSet):
    queryset = TeacherSalaryPayments.objects.all()
    serializer_class = TeacherSalaryPaymentsSerializer

@extend_schema(tags=["TeacherSalaryCalculations - O'qituvchi oyliklarini hisoblash "])
class TeacherSalaryCalculationsViewSet(viewsets.ModelViewSet):
    queryset = TeacherSalaryCalculations.objects.all()
    serializer_class = TeacherSalaryCalculationsSerializer