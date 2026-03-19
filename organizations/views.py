from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Sum, Count
from datetime import datetime

from audit.models import AuditLog
from .models import (
    Organizations, OrganizationSettings, Subscriptions, Branch,
    ExamSettings, LandingPage, LandingPageSubmission, Tag,
)
from .serializers import (
    OrganizationSerializer, OrganizationCreateSerializer,
    OrganizationSettingsSerializer, SubscriptionSerializer,
    BranchSerializer, ExamSettingsSerializer,
    BillingSubscriptionSerializer, BillingCreateSerializer,
    LandingPageSerializer, LandingPageCreateSerializer,
    LandingPageSubmissionSerializer, LandingPageSubmissionCreateSerializer,
    TagSerializer,
)


# ─── AuditLog helper ─────────────────────────────────────────────

def _log(entity_type, entity_id, action, old_data, new_data, user):
    try:
        employee = user.employee if hasattr(user, 'employee') else None
        AuditLog.objects.create(
            entity_type=entity_type,
            entity_id=entity_id,
            action=action,
            old_data=old_data,
            new_action=new_data,
            performed_by=employee,
            performed_by_role=employee.position if employee else '',
        )
    except Exception:
        pass


# ════════════════════════════════════════════════════════════════
#  ORGANIZATIONS
# ════════════════════════════════════════════════════════════════

@api_view(['GET', 'POST'])
def organization_list_create(request):
    if request.method == 'GET':
        status_filter = request.query_params.get('status')
        orgs          = Organizations.objects.all()
        if status_filter:
            orgs = orgs.filter(status=status_filter)
        return Response(OrganizationSerializer(orgs, many=True).data)

    serializer = OrganizationCreateSerializer(data=request.data)
    if serializer.is_valid():
        org = serializer.save()

        _log('other', org.id, 'create', None, {
            'action': 'Tashkilot yaratildi',
            'name':   org.name,
            'status': org.status,
        }, request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def organization_detail(request, pk):
    org = get_object_or_404(Organizations, pk=pk)

    if request.method == 'GET':
        return Response(OrganizationSerializer(org).data)

    elif request.method == 'PUT':
        old_data   = {'name': org.name, 'status': org.status}
        serializer = OrganizationSerializer(org, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            _log('other', org.id, 'update', old_data, {
                'name':   org.name,
                'status': org.status,
            }, request.user)

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        _log('other', org.id, 'delete', {'name': org.name}, None, request.user)
        org.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ════════════════════════════════════════════════════════════════
#  ORGANIZATION SETTINGS
# ════════════════════════════════════════════════════════════════

@api_view(['GET', 'PUT'])
def organization_settings(request, org_pk):
    org                  = get_object_or_404(Organizations, pk=org_pk)
    settings, created    = OrganizationSettings.objects.get_or_create(organization=org)

    if request.method == 'GET':
        return Response(OrganizationSettingsSerializer(settings).data)

    serializer = OrganizationSettingsSerializer(settings, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()

        _log('other', org.id, 'update', None, {
            'action': 'Tashkilot sozlamalari yangilandi',
        }, request.user)

        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ════════════════════════════════════════════════════════════════
#  SUBSCRIPTIONS
# ════════════════════════════════════════════════════════════════

@api_view(['GET', 'POST'])
def subscription_list_create(request, org_pk):
    org = get_object_or_404(Organizations, pk=org_pk)

    if request.method == 'GET':
        subs = Subscriptions.objects.filter(organization_id=org)
        return Response(SubscriptionSerializer(subs, many=True).data)

    serializer = SubscriptionSerializer(data=request.data)
    if serializer.is_valid():
        sub = serializer.save(organization_id=org)

        _log('other', sub.id, 'create', None, {
            'action':     'Obuna yaratildi',
            'plan_type':  sub.plan_type,
            'start_date': str(sub.start_date),
            'end_date':   str(sub.end_date),
            'status':     sub.status,
        }, request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def subscription_detail(request, org_pk, pk):
    sub = get_object_or_404(Subscriptions, pk=pk, organization_id__pk=org_pk)

    if request.method == 'GET':
        return Response(SubscriptionSerializer(sub).data)

    elif request.method == 'PUT':
        old_data   = {'status': sub.status, 'end_date': str(sub.end_date)}
        serializer = SubscriptionSerializer(sub, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            _log('other', sub.id, 'update', old_data, {
                'status':   sub.status,
                'end_date': str(sub.end_date),
            }, request.user)

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        _log('other', sub.id, 'delete', {'plan_type': sub.plan_type, 'status': sub.status}, None, request.user)
        sub.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ════════════════════════════════════════════════════════════════
#  BRANCHES
# ════════════════════════════════════════════════════════════════

@api_view(['GET', 'POST'])
def branch_list_create(request, org_pk):
    org = get_object_or_404(Organizations, pk=org_pk)

    if request.method == 'GET':
        is_active = request.query_params.get('is_active')
        branches  = Branch.objects.filter(organization_id=org)
        if is_active is not None:
            branches = branches.filter(is_active=is_active.lower() == 'true')
        return Response(BranchSerializer(branches, many=True).data)

    serializer = BranchSerializer(data=request.data)
    if serializer.is_valid():
        branch = serializer.save(organization_id=org)

        _log('other', branch.id, 'create', None, {
            'action': 'Filial yaratildi',
            'name':   branch.name,
            'phone':  branch.phone,
        }, request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def branch_detail(request, org_pk, pk):
    branch = get_object_or_404(Branch, pk=pk, organization_id__pk=org_pk)

    if request.method == 'GET':
        return Response(BranchSerializer(branch).data)

    elif request.method == 'PUT':
        old_data   = {'name': branch.name, 'is_active': branch.is_active}
        serializer = BranchSerializer(branch, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            _log('other', branch.id, 'update', old_data, {
                'name':      branch.name,
                'is_active': branch.is_active,
            }, request.user)

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        _log('other', branch.id, 'delete', {'name': branch.name}, None, request.user)
        branch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ════════════════════════════════════════════════════════════════
#  EXAM SETTINGS
# ════════════════════════════════════════════════════════════════

@api_view(['GET', 'PUT'])
def exam_settings(request, org_pk):
    org               = get_object_or_404(Organizations, pk=org_pk)
    settings, created = ExamSettings.objects.get_or_create(organization=org)

    if request.method == 'GET':
        return Response(ExamSettingsSerializer(settings).data)

    serializer = ExamSettingsSerializer(settings, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()

        _log('other', org.id, 'update', None, {
            'action': 'Imtihon sozlamalari yangilandi',
        }, request.user)

        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ════════════════════════════════════════════════════════════════
#  LANDING PAGES
# ════════════════════════════════════════════════════════════════

@api_view(['GET', 'POST'])
def landing_page_list_create(request, org_pk):
    org = get_object_or_404(Organizations, pk=org_pk)

    if request.method == 'GET':
        is_active = request.query_params.get('is_active')
        source    = request.query_params.get('source')
        pages     = LandingPage.objects.filter(organization=org)
        if is_active is not None:
            pages = pages.filter(is_active=is_active.lower() == 'true')
        if source:
            pages = pages.filter(source=source)
        return Response(LandingPageSerializer(pages, many=True).data)

    serializer = LandingPageCreateSerializer(data=request.data)
    if serializer.is_valid():
        page = serializer.save(organization=org)

        _log('other', page.id, 'create', None, {
            'action': 'Landing page yaratildi',
            'name':   page.name,
            'slug':   page.slug,
            'source': page.source,
        }, request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def landing_page_detail(request, org_pk, pk):
    page = get_object_or_404(LandingPage, pk=pk, organization__pk=org_pk)

    if request.method == 'GET':
        return Response(LandingPageSerializer(page).data)

    elif request.method == 'PUT':
        old_data   = {'name': page.name, 'is_active': page.is_active}
        serializer = LandingPageSerializer(page, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            _log('other', page.id, 'update', old_data, {
                'name':      page.name,
                'is_active': page.is_active,
            }, request.user)

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        _log('other', page.id, 'delete', {'name': page.name, 'slug': page.slug}, None, request.user)
        page.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def landing_page_by_slug(request, slug):
    page = get_object_or_404(LandingPage, slug=slug, is_active=True)
    return Response(LandingPageSerializer(page).data)


# ════════════════════════════════════════════════════════════════
#  LANDING PAGE SUBMISSIONS
# ════════════════════════════════════════════════════════════════

@api_view(['GET', 'POST'])
def submission_list_create(request, org_pk, page_pk):
    page = get_object_or_404(LandingPage, pk=page_pk, organization__pk=org_pk)

    if request.method == 'GET':
        submissions = LandingPageSubmission.objects.filter(landing_page=page)
        return Response(LandingPageSubmissionSerializer(submissions, many=True).data)

    serializer = LandingPageSubmissionCreateSerializer(data=request.data)
    if serializer.is_valid():
        sub = serializer.save(landing_page=page)

        _log('other', sub.id, 'create', None, {
            'action':    'Submission yaratildi',
            'full_name': sub.full_name,
            'phone':     sub.phone,
        }, request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def public_submission_create(request, slug):
    """Public endpoint — talabalar ro'yxatdan o'tishi (AuditLog shart emas)"""
    page = get_object_or_404(LandingPage, slug=slug, is_active=True)
    serializer = LandingPageSubmissionCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(landing_page=page)
        return Response({
            'message': "Arizangiz qabul qilindi! Tez orada siz bilan bog'lanamiz.",
            'data':    serializer.data,
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def submission_detail(request, org_pk, page_pk, pk):
    submission = get_object_or_404(
        LandingPageSubmission, pk=pk,
        landing_page__pk=page_pk, landing_page__organization__pk=org_pk,
    )

    if request.method == 'GET':
        return Response(LandingPageSubmissionSerializer(submission).data)

    _log('other', submission.id, 'delete', {
        'full_name': submission.full_name, 'phone': submission.phone,
    }, None, request.user)
    submission.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# ════════════════════════════════════════════════════════════════
#  STATISTIKA
# ════════════════════════════════════════════════════════════════

@api_view(['GET'])
def landing_statistics(request, org_pk):
    org   = get_object_or_404(Organizations, pk=org_pk)
    pages = LandingPage.objects.filter(organization=org)

    stats = [{
        'id':                page.id,
        'name':              page.name,
        'slug':              page.slug,
        'source':            page.source,
        'submissions_count': page.submissions.count(),
        'is_active':         page.is_active,
    } for page in pages]

    return Response(stats)


# ════════════════════════════════════════════════════════════════
#  BILLING
# ════════════════════════════════════════════════════════════════

@api_view(['GET'])
def billing_dashboard(request, org_pk):
    org         = get_object_or_404(Organizations, pk=org_pk)
    current_sub = Subscriptions.objects.filter(organization_id=org, status='active').order_by('-end_date').first()
    all_subs    = Subscriptions.objects.filter(organization_id=org)
    total_spent = all_subs.aggregate(total=Sum('price'))['total'] or 0

    days_remaining = 0
    if current_sub and current_sub.end_date:
        delta          = current_sub.end_date.date() - datetime.now().date()
        days_remaining = delta.days if delta.days > 0 else 0

    org_status = org.status
    if days_remaining == 0:
        org_status = 'expired'
    elif 0 < days_remaining <= 7:
        org_status = 'expires'

    return Response({
        'current_subscription': BillingSubscriptionSerializer(current_sub).data if current_sub else None,
        'total_subscriptions':  all_subs.count(),
        'total_spent':          total_spent,
        'next_payment_date':    current_sub.end_date if current_sub else None,
        'days_remaining':       days_remaining,
        'status':               org_status,
    })


@api_view(['GET'])
def billing_history(request, org_pk):
    org           = get_object_or_404(Organizations, pk=org_pk)
    subscriptions = Subscriptions.objects.filter(organization_id=org).order_by('-created_at')
    return Response(BillingSubscriptionSerializer(subscriptions, many=True).data)


@api_view(['POST'])
def billing_pay(request, org_pk):
    org        = get_object_or_404(Organizations, pk=org_pk)
    serializer = BillingCreateSerializer(data=request.data)
    if serializer.is_valid():
        subscription = serializer.save(organization_id=org)

        org.status = 'active'
        org.save()

        _log('other', subscription.id, 'create', None, {
            'action':    'To\'lov amalga oshirildi',
            'plan_type': subscription.plan_type,
            'price':     str(subscription.price),
            'end_date':  str(subscription.end_date),
        }, request.user)

        return Response({
            'message':      "To'lov muvaffaqiyatli amalga oshirildi!",
            'subscription': BillingSubscriptionSerializer(subscription).data,
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def billing_plans(request):
    plans = [
        {
            'plan_type': 'basic', 'name': 'Asosiy',
            'price_1month': 500000, 'price_3months': 1350000,
            'price_6months': 2400000, 'price_12months': 4500000,
            'features': ['50 tagacha guruh', '200 tagacha talaba', '5 ta filial', 'Asosiy hisobotlar'],
        },
        {
            'plan_type': 'premium', 'name': 'Premium',
            'price_1month': 1000000, 'price_3months': 2700000,
            'price_6months': 4800000, 'price_12months': 9000000,
            'features': ['Cheksiz guruh', 'Cheksiz talaba', 'Cheksiz filial',
                         'Barcha hisobotlar', 'SMS xizmati', 'Prioritet qo\'llab-quvvatlash'],
        },
        {
            'plan_type': 'enterprise', 'name': 'Korporativ',
            'price_1month': 2000000, 'price_3months': 5400000,
            'price_6months': 9600000, 'price_12months': 18000000,
            'features': ['Premium barcha imkoniyatlari', 'Maxsus integratsiyalar',
                         'Shaxsiy menejer', 'API kirish', 'White-label imkoniyati'],
        },
    ]
    return Response(plans)


@api_view(['GET'])
def billing_current(request, org_pk):
    org         = get_object_or_404(Organizations, pk=org_pk)
    current_sub = Subscriptions.objects.filter(organization_id=org, status='active').order_by('-end_date').first()

    if not current_sub:
        return Response({'message': 'Faol obuna topilmadi'}, status=status.HTTP_404_NOT_FOUND)

    return Response(BillingSubscriptionSerializer(current_sub).data)


# ════════════════════════════════════════════════════════════════
#  TAGS
# ════════════════════════════════════════════════════════════════

class TagListCreateView(generics.ListCreateAPIView):
    queryset         = Tag.objects.all()
    serializer_class = TagSerializer

    def get_queryset(self):
        object_type = self.request.query_params.get('object_type')
        if object_type:
            return self.queryset.filter(object_type=object_type)
        return self.queryset

    def perform_create(self, serializer):
        tag = serializer.save()
        _log('other', tag.id, 'create', None, {
            'action':      'Tag yaratildi',
            'name':        tag.name,
            'object_type': tag.object_type,
        }, self.request.user)


class TagRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset         = Tag.objects.all()
    serializer_class = TagSerializer

    def perform_update(self, serializer):
        old = {'name': serializer.instance.name}
        tag = serializer.save()
        _log('other', tag.id, 'update', old, {'name': tag.name}, self.request.user)

    def perform_destroy(self, instance):
        _log('other', instance.id, 'delete', {'name': instance.name, 'object_type': instance.object_type},
             None, self.request.user)
        instance.delete()


