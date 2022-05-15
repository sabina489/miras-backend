from rest_framework import permissions


class IsEnrollmentOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.student == request.user
