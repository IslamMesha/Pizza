from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsDeliveredOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return bool(False if obj.status == "delivered" else True)
