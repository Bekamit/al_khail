from django import forms
from django.contrib import admin
from django.core.validators import FileExtensionValidator

from service.admin import CustomModelAdmin
from apps.project.models import Project, Facilities


class ProjectAdminForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

    def clean_pdf_catalog(self):
        pdf = self.cleaned_data.get('pdf_catalog')
        validator = FileExtensionValidator(allowed_extensions=['pdf'])
        validator(pdf)
        return pdf


@admin.register(Project)
class ProjectTypeAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    list_display = ('name',
                    'pdf_catalog',
                    'estate_objects',)
    search_fields = ('name',
                     'location',)
    fields = (
        'name',
        'facilities',
        'location',
        'completion',
        'is_furnished',
        'pdf_catalog',
    )

    def estate_objects(self, project):
        return project.estate.all().count()


@admin.register(Facilities)
class FacilitiesAdmin(CustomModelAdmin):
    form = ProjectAdminForm
    list_display = ('type',
                    'icon',)
    search_fields = ('type',)
    fieldsets = [
        ('English', {
            'fields': [
                'type_en',
                'icon',
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
