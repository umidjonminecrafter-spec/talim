from django.urls import path
from . import views
from .views import TagListCreateView, TagRetrieveUpdateDeleteView

urlpatterns = [
    # Organizations
    path('organizations/', views.organization_list_create, name='organization-list-create'),
    path('organizations/<int:pk>/', views.organization_detail, name='organization-detail'),

    # Organization Settings
    path('organizations/<int:org_pk>/settings/', views.organization_settings, name='organization-settings'),

    # Subscriptions
    path('organizations/<int:org_pk>/subscriptions/', views.subscription_list_create, name='subscription-list-create'),
    path('organizations/<int:org_pk>/subscriptions/<int:pk>/', views.subscription_detail, name='subscription-detail'),

    # Branches
    path('organizations/<int:org_pk>/branches/', views.branch_list_create, name='branch-list-create'),
    path('organizations/<int:org_pk>/branches/<int:pk>/', views.branch_detail, name='branch-detail'),

    # Exam Settings
    path('organizations/<int:org_pk>/exam-settings/', views.exam_settings, name='exam-settings'),

    # Landing Pages
    path('organizations/<int:org_pk>/landing-pages/', views.landing_page_list_create, name='landing-page-list-create'),
    path('organizations/<int:org_pk>/landing-pages/<int:pk>/', views.landing_page_detail, name='landing-page-detail'),
    path('organizations/<int:org_pk>/landing-statistics/', views.landing_statistics, name='landing-statistics'),

    # Landing Page Submissions (Admin)
    path('organizations/<int:org_pk>/landing-pages/<int:page_pk>/submissions/', views.submission_list_create,
         name='submission-list-create'),
    path('organizations/<int:org_pk>/landing-pages/<int:page_pk>/submissions/<int:pk>/', views.submission_detail,
         name='submission-detail'),

    # Public Endpoints (talabalar uchun)
    path('landing/<slug:slug>/', views.landing_page_by_slug, name='landing-page-by-slug'),
    path('landing/<slug:slug>/submit/', views.public_submission_create, name='public-submission-create'),

    # Billing Dashboard
    path('organizations/<int:org_pk>/billing/', views.billing_dashboard, name='billing-dashboard'),

    # Joriy obuna
    path('organizations/<int:org_pk>/billing/current/', views.billing_current, name='billing-current'),

    # To'lov tarixi
    path('organizations/<int:org_pk>/billing/history/', views.billing_history, name='billing-history'),

    # To'lov qilish
    path('organizations/<int:org_pk>/billing/pay/', views.billing_pay, name='billing-pay'),

    # Tariflar ro'yxati (Public)
    path('billing/plans/', views.billing_plans, name='billing-plans'),
    path("tags/", TagListCreateView.as_view(), name="tag-list-create"),
    path("tags/<int:pk>/", TagRetrieveUpdateDeleteView.as_view(), name="tag-detail"),

]