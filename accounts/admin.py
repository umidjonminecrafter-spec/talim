from django.contrib import admin
from accounts.models import Employee, Role, RolePermission, UserRole, User
from core.admin import BaseModelAdmin
# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(BaseModelAdmin):
    list_display = ["user", "photo", "position", "is_active"]
    list_filter = ["user", "position", "is_active"]
    search_fields = ["user", "position", "is_active"]
