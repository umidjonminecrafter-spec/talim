from django.db import models
from core.models import BaseModel
class ExpenseCategory(BaseModel):
    name = models.CharField(max_length=250)

class Expenses(BaseModel):
    category = models.ForeignKey(ExpenseCategory, on_delete=models.SET_NULL, null=True, related_name="category")
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    expense_date = models.DateTimeField()
    comment = models.TextField()

