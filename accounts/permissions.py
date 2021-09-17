from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserOwnerPermission(BasePermission):
    def has_permission(self, request, view):
        if request.methods in SAFE_METHODS:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj == request.user