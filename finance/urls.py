from django.urls import path
from .views import ExpenseCategoryViewSet, ExpensesViewSet

urlpatterns = [
    # ExpenseCategory URLs
    path('expense-categories/', ExpenseCategoryViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='expensecategory-list'),
    path('expense-categories/<int:pk>/', ExpenseCategoryViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='expensecategory-detail'),

    # Expenses URLs
    path('expenses/', ExpensesViewSet.as_view({'get': 'list', 'post': 'create'}), name='expenses-list'),
    path('expenses/<int:pk>/',
         ExpensesViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='expenses-detail'),
]