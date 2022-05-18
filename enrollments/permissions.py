from rest_framework import permissions

from .api.utils import (
    is_enrolled_active,
    is_enrolled,
)


class IsEnrolledActive(permissions.BasePermission):
    """Permission to allow only the enrolled users to use the obj."""
    code = "NO ACTIVE ENROLLMENT"
    message = "You don't have active enrollment."

    def has_object_permission(self, request, view, obj):
        return is_enrolled_active(obj, request.user)


class IsEnrolled(permissions.BasePermission):
    code = "ALREADY ENROLLED"
    message = "You already have an enrollment."

    def has_object_permission(self, request, view, obj):
        return is_enrolled(obj, request.user)
