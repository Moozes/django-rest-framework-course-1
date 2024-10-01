from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        admin_permission = super().has_permission(request, view)
        return request.method == 'GET' or admin_permission

class OwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # Check permissions for read-only request
            return True
        else:
            # Check permissions for write request
            print(f"request.user: {request.user}")
            print(f"obj.user: {obj.user}")
            return request.user == obj.user