from django.urls import path

from .views import (
    StudentViewSet, StudentGroupViewSet, StudentPricingViewSet,
    StudentBalancesViewSet, StudentTarnsactionsViewSet, LeaveReasonViewSet,
    StudentGroupLeavesViewSet, StudentFreezesViewSet, StudentBalanceHistoryViewSet,
    AttendenceViewSet, RoomViewSet, CourseViewSet, GroupViewSet,
    GroupTeacherViewSet, LessonTimeViewSet, LessonScheduleViewSet,
    ExamsViewSet, ExamResultsViewSet,
    TeacherSalaryRulesViewSet, TeacherSalaryPaymentsViewSet, TeacherSalaryCalculationsViewSet
)

urlpatterns = [
    # ==================== STUDENT URLs ====================
    path('students/', StudentViewSet.as_view({'get': 'list', 'post': 'create'}), name='student-list'),
    path('students/<int:pk>/',
         StudentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='student-detail'),

    path('student-groups/', StudentGroupViewSet.as_view({'get': 'list', 'post': 'create'}), name='studentgroup-list'),
    path('student-groups/<int:pk>/', StudentGroupViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='studentgroup-detail'),

    path('student-pricings/', StudentPricingViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='studentpricing-list'),
    path('student-pricings/<int:pk>/', StudentPricingViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='studentpricing-detail'),

    path('student-balances/', StudentBalancesViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='studentbalances-list'),
    path('student-balances/<int:pk>/', StudentBalancesViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='studentbalances-detail'),

    path('student-transactions/', StudentTarnsactionsViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='studenttransactions-list'),
    path('student-transactions/<int:pk>/', StudentTarnsactionsViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='studenttransactions-detail'),

    path('leave-reasons/', LeaveReasonViewSet.as_view({'get': 'list', 'post': 'create'}), name='leavereason-list'),
    path('leave-reasons/<int:pk>/', LeaveReasonViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='leavereason-detail'),

    path('student-group-leaves/', StudentGroupLeavesViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='studentgroupleaves-list'),
    path('student-group-leaves/<int:pk>/', StudentGroupLeavesViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='studentgroupleaves-detail'),

    path('student-freezes/', StudentFreezesViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='studentfreezes-list'),
    path('student-freezes/<int:pk>/', StudentFreezesViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='studentfreezes-detail'),

    path('student-balance-history/', StudentBalanceHistoryViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='studentbalancehistory-list'),
    path('student-balance-history/<int:pk>/', StudentBalanceHistoryViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='studentbalancehistory-detail'),

    path('attendences/', AttendenceViewSet.as_view({'get': 'list', 'post': 'create'}), name='attendence-list'),
    path('attendences/<int:pk>/', AttendenceViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='attendence-detail'),

    # ==================== GROUP URLs ====================
    path('rooms/', RoomViewSet.as_view({'get': 'list', 'post': 'create'}), name='room-list'),
    path('rooms/<int:pk>/',
         RoomViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='room-detail'),

    path('courses/', CourseViewSet.as_view({'get': 'list', 'post': 'create'}), name='course-list'),
    path('courses/<int:pk>/',
         CourseViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='course-detail'),

    path('groups/', GroupViewSet.as_view({'get': 'list', 'post': 'create'}), name='group-list'),
    path('groups/<int:pk>/',
         GroupViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='group-detail'),

    path('group-teachers/', GroupTeacherViewSet.as_view({'get': 'list', 'post': 'create'}), name='groupteacher-list'),
    path('group-teachers/<int:pk>/', GroupTeacherViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='groupteacher-detail'),

    # ==================== LESSON URLs ====================
    path('lesson-times/', LessonTimeViewSet.as_view({'get': 'list', 'post': 'create'}), name='lessontime-list'),
    path('lesson-times/<int:pk>/', LessonTimeViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='lessontime-detail'),

    path('lesson-schedules/', LessonScheduleViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='lessonschedule-list'),
    path('lesson-schedules/<int:pk>/', LessonScheduleViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='lessonschedule-detail'),

    path('exams/', ExamsViewSet.as_view({'get': 'list', 'post': 'create'}), name='exams-list'),
    path('exams/<int:pk>/',
         ExamsViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='exams-detail'),

    path('exam-results/', ExamResultsViewSet.as_view({'get': 'list', 'post': 'create'}), name='examresults-list'),
    path('exam-results/<int:pk>/', ExamResultsViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='examresults-detail'),


    # ==================== TEACHER URLs ====================
    path('teacher-salary-rules/', TeacherSalaryRulesViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='teachersalaryrules-list'),
    path('teacher-salary-rules/<int:pk>/', TeacherSalaryRulesViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='teachersalaryrules-detail'),

    path('teacher-salary-payments/', TeacherSalaryPaymentsViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='teachersalarypayments-list'),
    path('teacher-salary-payments/<int:pk>/', TeacherSalaryPaymentsViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='teachersalarypayments-detail'),

    path('teacher-salary-calculations/', TeacherSalaryCalculationsViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='teachersalarycalculations-list'),
    path('teacher-salary-calculations/<int:pk>/', TeacherSalaryCalculationsViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='teachersalarycalculations-detail'),
]