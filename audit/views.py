from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from academics.models.group import Group

from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Q
from django.utils import timezone

from .models import AuditLog
from .serializers import AuditLogSerializer, AttendanceReportSerializer, AttendanceReportFilterSerializer
from academics.models import StudentGroup


# ════════════════════════════════════════════════════════════════
#  AUDIT LOG VIEWSET
#  (Bu yerda AuditLog yozish shart emas — bu o'zi saqlovchi model)
# ════════════════════════════════════════════════════════════════

@extend_schema(tags=["AuditLog - Barcha bajarilgan ishlarni saqlab boradi"])
class AuditLogViewSet(viewsets.ModelViewSet):
    queryset         = AuditLog.objects.all().order_by('-created_at')
    serializer_class = AuditLogSerializer

    # AuditLog ni o'zi o'qish uchun — yozish kerak emas
    http_method_names = ['get', 'head', 'options']


# ════════════════════════════════════════════════════════════════
#  DAVOMAT HISOBOTI  v1
# ════════════════════════════════════════════════════════════════

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def attendance_report(request):
    filter_serializer = AttendanceReportFilterSerializer(data=request.data)

    if not filter_serializer.is_valid():
        return Response({'success': False, 'errors': filter_serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)

    start_date = filter_serializer.validated_data['start_date']
    end_date   = filter_serializer.validated_data['end_date']
    group_id   = filter_serializer.validated_data.get('group_id')

    group = None
    if group_id:
        try:
            group = Group.objects.get(pk=group_id)
        except Group.DoesNotExist:
            return Response({'success': False, 'message': 'Guruh topilmadi.'},
                            status=status.HTTP_404_NOT_FOUND)

    student_groups = StudentGroup.objects.filter(left_at__isnull=True)
    if group:
        student_groups = student_groups.filter(group=group)

    total_students = student_groups.count()

    # Kelgan (eng kam 1 marta)
    came_once = student_groups.filter(
        A_Sgroup__lesson_date__range=[start_date, end_date],
        A_Sgroup__is_present=True
    ).distinct().count()

    # Kelmagan
    not_came_ids = []
    for sg in student_groups:
        attendances = sg.A_Sgroup.filter(lesson_date__range=[start_date, end_date])
        if attendances.exists():
            if not attendances.filter(is_present=True).exists():
                not_came_ids.append(sg.id)
        else:
            not_came_ids.append(sg.id)

    not_came = len(not_came_ids)

    # Belgilanmagan
    marked_students = student_groups.filter(
        A_Sgroup__lesson_date__range=[start_date, end_date]
    ).distinct().count()
    not_marked = total_students - marked_students

    report_data = {
        'indicator_name': 'Davomat',
        'description':    'Talabalar davomat statistikasi',
        'came_once':      came_once,
        'not_came':       not_came,
        'not_marked':     not_marked,
        'total':          total_students,
    }

    return Response({
        'success': True,
        'filters': {
            'start_date': str(start_date),
            'end_date':   str(end_date),
            'group_name': group.name if group else 'Barcha guruhlar',
        },
        'data': [AttendanceReportSerializer(report_data).data],
    })


# ════════════════════════════════════════════════════════════════
#  FAOL GURUHLAR RO'YXATI  (filter dropdown uchun)
# ════════════════════════════════════════════════════════════════

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def active_groups_list(request):
    groups = Group.objects.filter(status='active').values('id', 'name').order_by('name')
    return Response({'success': True, 'data': list(groups)})


# ════════════════════════════════════════════════════════════════
#  DAVOMAT HISOBOTI  v2  (yaxshilangan)
# ════════════════════════════════════════════════════════════════

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def attendance_report_v2(request):
    start_date = request.data.get('start_date')
    end_date   = request.data.get('end_date')
    group_id   = request.data.get('group_id')

    if not start_date or not end_date:
        return Response({'success': False, 'message': 'start_date va end_date majburiy.'},
                        status=status.HTTP_400_BAD_REQUEST)

    group = None
    if group_id:
        try:
            group = Group.objects.get(pk=group_id)
        except Group.DoesNotExist:
            return Response({'success': False, 'message': 'Guruh topilmadi.'},
                            status=status.HTTP_404_NOT_FOUND)

    student_groups = StudentGroup.objects.filter(
        left_at__isnull=True,
        joined_at__lte=end_date,
    )
    if group:
        student_groups = student_groups.filter(group=group)

    total_students = student_groups.count()
    came_once = not_came = not_marked = 0

    for sg in student_groups:
        attendances = sg.A_Sgroup.filter(lesson_date__range=[start_date, end_date])
        if not attendances.exists():
            not_marked += 1
        elif attendances.filter(is_present=True).exists():
            came_once += 1
        else:
            not_came += 1

    report_data = {
        'indicator_name': 'Davomat hisoboti',
        'description':    f'{start_date} dan {end_date} gacha davomat statistikasi',
        'came_once':      came_once,
        'not_came':       not_came,
        'not_marked':     not_marked,
        'total':          total_students,
    }

    return Response({
        'success': True,
        'filters': {
            'start_date': start_date,
            'end_date':   end_date,
            'group_id':   group_id,
            'group_name': group.name if group else 'Barcha guruhlar',
        },
        'data': report_data,
        'breakdown': {
            'came_once_percent':  round((came_once  / total_students * 100) if total_students > 0 else 0, 2),
            'not_came_percent':   round((not_came   / total_students * 100) if total_students > 0 else 0, 2),
            'not_marked_percent': round((not_marked / total_students * 100) if total_students > 0 else 0, 2),
        },
    })


# ════════════════════════════════════════════════════════════════
#  BATAFSIL DAVOMAT HISOBOTI  (har bir talaba uchun)
# ════════════════════════════════════════════════════════════════

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def detailed_attendance_report(request):
    start_date = request.data.get('start_date')
    end_date   = request.data.get('end_date')
    group_id   = request.data.get('group_id')

    if not start_date or not end_date:
        return Response({'success': False, 'message': 'start_date va end_date majburiy.'},
                        status=status.HTTP_400_BAD_REQUEST)

    group = None
    if group_id:
        try:
            group = Group.objects.get(pk=group_id)
        except Group.DoesNotExist:
            return Response({'success': False, 'message': 'Guruh topilmadi.'},
                            status=status.HTTP_404_NOT_FOUND)

    student_groups = StudentGroup.objects.filter(
        left_at__isnull=True,
        joined_at__lte=end_date,
    ).select_related('student', 'group')
    if group:
        student_groups = student_groups.filter(group=group)

    students_data = []
    for sg in student_groups:
        attendances  = sg.A_Sgroup.filter(lesson_date__range=[start_date, end_date])
        attended     = attendances.filter(is_present=True).count()
        missed       = attendances.filter(is_present=False).count()
        total_marked = attendances.count()
        rate         = round((attended / total_marked * 100), 2) if total_marked > 0 else 0

        students_data.append({
            'student_id':      sg.student.id,
            'student_name':    sg.student.full_name,
            'group_name':      sg.group.name,
            'total_lessons':   total_marked,
            'attended':        attended,
            'missed':          missed,
            'not_marked':      0,
            'attendance_rate': rate,
        })

    return Response({
        'success': True,
        'filters': {
            'start_date': start_date,
            'end_date':   end_date,
            'group_name': group.name if group else 'Barcha guruhlar',
        },
        'count':    len(students_data),
        'students': students_data,
    })