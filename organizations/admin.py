from django.contrib import admin

from core.admin import BaseModelAdmin
from organizations.models import Branch, Organizations, Subscriptions
# Register your models here.

@admin.register(Organizations)
class OrganizationsAdmin(BaseModelAdmin):
    list_display = ["name", "logo", "address", "phone", "status", "created_at"]
    list_filter = ["name", "address", "phone", "status", "created_at"]
    search_fields = ["name", "address", "phone", "status", "created_at"]