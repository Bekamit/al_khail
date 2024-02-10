from django.contrib import admin


class CustomModelAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('css/admin.css',),
        }

    def not_null_fields(self, obj):
        return all([getattr(obj, field.name) for field in obj._meta.fields if field.name != 'id'])
    not_null_fields.boolean = True
    not_null_fields.short_description = 'All fields are filled'


class ReadDeleteModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return True

    def get_readonly_fields(self, request, obj=None):
        return [field.name for field in self.model._meta.fields]

    def date(self, obj):
        return f'#{obj.pk} | {obj.created_at.strftime("%Y-%m-%d, %H:%M")}'
