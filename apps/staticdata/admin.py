from django.contrib import admin
from .models import StaticData

@admin.register(StaticData)
class StaticDataAdmin(admin.ModelAdmin):
    list_display = ['field1', 'field2']
    fields = ['field1', 'field2']

    def has_add_permission(self, request):
        # Отключает кнопку "Добавить" для объекта Singleton
        return False

    def has_delete_permission(self, request, obj=None):
        # Отключает кнопку "Удалить" для объекта Singleton
        return False

    def save_model(self, request, obj, form, change):
        # Принудительно устанавливаем pk на 1 при сохранении
        obj.pk = 1
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        # Возвращает QuerySet с единственным объектом
        return super().get_queryset(request).filter(pk=1)
