from django.contrib import admin
from apps.analytics.models import Analytics, Role


admin.site.register(Role)
admin.site.register(Analytics)
