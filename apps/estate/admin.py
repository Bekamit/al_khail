from django.utils.safestring import mark_safe
from django.contrib import admin
from .models import EstateType, Estate, EstateImage, Project


class EstateImageInline(admin.TabularInline):
    model = EstateImage
    extra = 1


@admin.register(Estate)
class EstateAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'project',
                    'area',
                    'estate_type',
                    'city',
                    'is_secondary',
                    'preview')
    search_fields = ('project__name', 'title', 'developer', 'district', 'estate_type__type_en', 'city__city_name_en')
    list_filter = ('city__city_name', 'project__name', 'estate_type__type', 'is_secondary')
    fieldsets = [
        ('English', {
            'fields': [
                'project',
                'title_en',
                'developer_en',
                'area',
                'district_en',
                'description_en',
                'estate_type',
                'city',
                'is_secondary',
            ],
        }),
        ('Arabic', {
            'fields': [
                'title_ar',
                'developer_ar',
                'district_ar',
                'description_ar',
            ]
        }),
        ('Turkish', {
            'fields': [
                'title_tr',
                'developer_tr',
                'district_tr',
                'description_tr',
            ]
        }),
        ('Russian', {
            'fields': [
                'title_ru',
                'developer_ru',
                'district_ru',
                'description_ru',
            ],
        })
    ]
    inlines = [EstateImageInline]

    class Media:
        css = {
            'all': ('css/admin.css',),
        }

    def preview(self, obj):
        return mark_safe(f'<button class="btn btn-primary" style=margin-left: 15px;">look up</button>')


@admin.register(EstateType)
class EstateTypeAdmin(admin.ModelAdmin):
    list_display = ('type',)
    search_fields = ('type', 'type_ar', 'type_tr', 'type_ru')
    fieldsets = [
        ('English', {
            'fields': [
                'type_en',
            ],
        }),
        ('Arabic', {
            'fields': [
                'type_ar',
            ]
        }),
        ('Turkish', {
            'fields': [
                'type_tr',
            ]
        }),
        ('Russian', {
            'fields': [
                'type_ru',
            ],
        })
    ]

    class Media:
        css = {
            'all': ('css/admin.css',),
        }


@admin.register(Project)
class ProjectTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    fields = (
            'name',
            'pdf_catalog',
    )
