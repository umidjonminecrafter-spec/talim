from django.contrib import admin
from django.utils.html import format_html


class BaseModelAdmin(admin.ModelAdmin):
    """Barcha admin classlar uchun base class"""

    # Umumiy sozlamalar
    list_per_page = 15
    save_on_top = True
    show_full_result_count = True

    # Avtomatik sanalarni ko'rsatish
    def get_list_display(self, request):
        list_display = list(super().get_list_display(request))
        if 'created_at' in [f.name for f in self.model._meta.fields]:
            if 'created_at' not in list_display:
                list_display.append('created_at')
        if 'updated_at' in [f.name for f in self.model._meta.fields]:
            if 'updated_at' not in list_display:
                list_display.append('updated_at')
        return list_display

    # Avtomatik readonly fields
    def get_readonly_fields(self, request, obj=None):
        readonly = list(super().get_readonly_fields(request, obj))
        if obj:  # Editing
            readonly.extend(['created_at', 'updated_at', 'created_by', 'updated_by'])
        return readonly

    # Avtomatik search fields
    def get_search_fields(self, request):
        search_fields = list(super().get_search_fields(request))
        # Agar 'name' maydoni bo'lsa
        if 'name' in [f.name for f in self.model._meta.fields]:
            if 'name' not in search_fields:
                search_fields.append('name')
        # Agar 'title' maydoni bo'lsa
        if 'title' in [f.name for f in self.model._meta.fields]:
            if 'title' not in search_fields:
                search_fields.append('title')
        return search_fields

    # Status uchun rangli badge
    def status_badge(self, obj):
        if hasattr(obj, 'status'):
            colors = {
                'active': 'green',
                'inactive': 'red',
                'pending': 'orange',
            }
            color = colors.get(obj.status, 'gray')
            return format_html(
                '<span style="background-color: {}; color: white; padding: 3px 10px; border-radius: 3px;">{}</span>',
                color, obj.status.upper()
            )
        return '-'

    status_badge.short_description = 'Status'

    # Avtomatik save qilishda user ni saqlash
    def save_model(self, request, obj, form, change):
        if not change:  # Yangi obyekt
            if hasattr(obj, 'created_by'):
                obj.created_by = request.user
        if hasattr(obj, 'updated_by'):
            obj.updated_by = request.user
        super().save_model(request, obj, form, change)