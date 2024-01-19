from django.contrib import admin


class CustomModelAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('css/admin.css',),
        }