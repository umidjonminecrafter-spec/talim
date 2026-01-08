from django.urls import path
from .views import (
    OrganizationsListCreate,
    OrganizationsRetrieveUpdateDestroy,
    SubscriptionsListCreate,
    SubscriptionsRetrieveUpdateDestroy,
    BranchListCreate,
    BranchRetrieveUpdateDestroy
)

urlpatterns = [
    path('organizations/', OrganizationsListCreate.as_view()),
    path('organizations/<int:pk>/', OrganizationsRetrieveUpdateDestroy.as_view()),
    path('subscriptions/', SubscriptionsListCreate.as_view()),
    path('subscriptions/<int:pk>/', SubscriptionsRetrieveUpdateDestroy.as_view()),
    path('branch/', BranchListCreate.as_view()),
    path('branch/<int:pk>/', BranchRetrieveUpdateDestroy.as_view())
]