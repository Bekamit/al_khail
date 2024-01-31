from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

class CustomModelAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    summernote_fields = '__all__'
    class Media:
        css = {
            'all': ('css/admin.css',),
        }