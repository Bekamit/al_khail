from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ("email", "is_staff", "is_active", "language")
    list_filter = ("email",)
    fieldsets = (
        ("User:", {"fields": ("email", "password", "language")}),
        ("Permissions:", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        ("New User:", {"classes": ("wide",),
                       "fields": ("email",
                                  "password1",
                                  "password2",
                                  "is_staff",
                                  "is_active",
                                  "user_permissions")}),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.unregister(Group)
