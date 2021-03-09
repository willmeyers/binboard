from rest_framework import permissions


class ActionBasedPermissions(permissions.AllowAny):
    def has_permission(self, request, view):
        for permission_class, actions in getattr(view, 'action_permissions', {}).items():
            if view.action in actions:
                return permission_class().has_permission(request, view)

        return False


class IsStaffOrAdmin(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        user = request.user

        if user.is_staff:
            return True

        return False
