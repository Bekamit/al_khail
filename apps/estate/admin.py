from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from django.contrib import admin

from service.admin import CustomModelAdmin
from .models import EstateType, Estate, EstateImage


class EstateImageInline(admin.TabularInline):
    model = EstateImage
    extra = 1


@admin.register(Estate)
class EstateAdmin(CustomModelAdmin):
    list_display = ('id',
                    'title',
                    'project',
                    'area',
                    'estate_type',
                    'city',
                    'visits',
                    'preview',
                    'test_to_show',
                    'is_active',)
    list_editable = ['is_active']
    actions = ['in_show']
    search_fields = ('project__name', 'title_en', 'estate_type__type_en', 'city__city_name_en')
    list_filter = ('city__city_name', 'project__name', 'estate_type__type', 'is_secondary')
    fieldsets = [
        ('English', {
            'fields': [
                'project',
                'title_en',
                'area',
                'description_en',
                'price_usd',
                'estate_type',
                'city',
                'is_secondary',
            ],
        }),
        ('Arabic', {
            'fields': [
                'title_ar',
                'description_ar',
            ]
        }),
        ('Turkish', {
            'fields': [
                'title_tr',
                'description_tr',
            ]
        }),
        ('Russian', {
            'fields': [
                'title_ru',
                'description_ru',
            ],
        })
    ]
    inlines = [EstateImageInline]

    def preview(self, obj):
        return mark_safe(f'<button class="btn btn-primary" style=margin-left: 15px;">look up</button>')

    def in_show(self, request, queryset):
        queryset.update(is_active=not queryset.first().is_active)

    in_show.short_description = _("Add/pop from site")

    def has_photo(self, obj):
        return obj.images.all().count()

    def test_to_show(self, obj):
        return mark_safe(f"<small>{'✅' if self.not_null_fields(obj) else '⛔'} All fields</small><br>"
                         f"<small>{'✅' if self.has_photo(obj) else '⛔'} All photos: {self.has_photo(obj)}</small>")


@admin.register(EstateType)
class EstateTypeAdmin(CustomModelAdmin):
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
