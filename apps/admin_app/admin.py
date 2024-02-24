
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group


from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ()
    list_filter = ()

    fieldsets = [
                (None, {"fields": ("email", "password", "language")}),
            ]
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "language", "is_staff", "is_superuser"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)

    def get_list_display(self, request):
        list_display = super(CustomUserAdmin, self).get_list_display(request)
        if request.user.is_superuser:
            return ("email", "is_staff", "language", "is_superuser")
        else:
            return ("language",)

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if request.user.is_superuser:
            return [
                (None, {"fields": ("email", "password", "language")}),
                ("Permissions", {"fields": ("is_staff", "is_superuser", "user_permissions")}),
            ]
        else:
            return [
                (None, {"fields": ("language", )}),
            ]

    def has_module_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(email=request.user.email)


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.unregister(Group)
