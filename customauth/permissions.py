from rest_framework import permissions


class CurrentUser(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        user = request.user
        return obj.pk == user.pk


class DenyAny(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        return False
