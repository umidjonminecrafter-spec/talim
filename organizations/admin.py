from django.contrib import admin

from core.admin import BaseModelAdmin
from organizations.models import Branch, Organizations, Subscriptions
# Register your models here.

@admin.register(Organizations)
class OrganizationsAdmin(BaseModelAdmin):
    list_display = ["name", "logo", "address", "phone", "status"]
    list_filter = ["name", "address", "phone", "status"]
    search_fields = ["name", "address", "phone", "status"]
    readonly_fields = ('created_at',)


@admin.register(Branch)
class BranchAdmin(BaseModelAdmin):
    list_display = ["organization_id", "name", "address", "phone", "is_active"]
    list_filter = ["name", "address", "phone", "is_active"]
    search_fields = ["name", "address", "phone", "is_active"]
    readonly_fields = ('created_at',)

@admin.register(Subscriptions)
class SubscriptionsAdmin(BaseModelAdmin):
    list_display = ["organization_id", "plan_type", "start_date", "end_date", "status", "price"]
    list_filter = ["organization_id", "plan_type", "start_date", "status", "end_date"]
    search_fields = ["plan_type", "start_date", "end_date", "status", "price"]
    readonly_fields = ('created_at',)
