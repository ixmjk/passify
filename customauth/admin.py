from django.contrib import admin
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import TokenProxy

from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):

    list_display = [
        "id",
        "first_name",
        "last_name",
        "email",
    ]

    list_filter = [
        "date_joined",
        "last_login",
        "is_active",
        "is_admin",
    ]

    list_per_page = 10

    search_fields = [
        "id__istartswith",
        "first_name__istartswith",
        "last_name__istartswith",
        "email__istartswith",
    ]

    def has_add_permission(self, request, obj=None):
        return True

    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        if obj:  # Change user
            if obj.is_admin:
                return False
            else:
                return True
        else:  # Add user
            return True

    def has_delete_permission(self, request, obj=None):
        return False

    def get_exclude(self, request, obj=None):
        if obj:  # Change user
            exclude = [
                "password",
            ]
        else:  # Add user
            exclude = []
        return exclude

    def get_readonly_fields(self, request, obj=None):
        if obj:  # Change user
            if obj.is_admin:
                readonly_fields = [
                    field.name for field in self.model._meta.get_fields()
                ]
            else:
                readonly_fields = [
                    "id",
                    "first_name",
                    "last_name",
                    "date_joined",
                    "last_login",
                    "is_admin",
                ]
        else:  # Add user
            readonly_fields = [
                "date_joined",
                "last_login",
                "is_admin",
            ]

        return readonly_fields

    def get_fieldsets(self, request, obj=None):
        if obj:  # Change user
            fieldsets = (
                (
                    "Account Information",
                    {
                        "fields": (
                            "id",
                            "first_name",
                            "last_name",
                            "email",
                            "date_joined",
                            "last_login",
                        )
                    },
                ),
                (
                    "Account Settings",
                    {
                        "fields": (
                            "is_active",
                            "is_admin",
                        ),
                        "classes": ("collapse",),
                    },
                ),
            )
        else:  # Add user
            fieldsets = (
                (
                    "Account Information",
                    {
                        "fields": (
                            "first_name",
                            "last_name",
                            "email",
                            "password",
                            "date_joined",
                            "last_login",
                        )
                    },
                ),
                (
                    "Account Settings",
                    {
                        "fields": (
                            "is_active",
                            "is_admin",
                        ),
                        "classes": ("collapse",),
                    },
                ),
            )
        return fieldsets


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)
