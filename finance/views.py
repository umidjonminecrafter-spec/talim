from django.shortcuts import render
from drf_spectacular.utils import extend_schema

# Create your views here.
from rest_framework import viewsets
from .models import ExpenseCategory, Expenses
from .serializers import ExpenseCategorySerializer, ExpensesSerializer

@extend_schema(tags=["ExpenseCategory - Harajatlar kategoriyasini ko'rish "])
class ExpenseCategoryViewSet(viewsets.ModelViewSet):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer

@extend_schema(tags=["Expenses - Harajatlar larni barchasini ko'rish"])
class ExpensesViewSet(viewsets.ModelViewSet):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer