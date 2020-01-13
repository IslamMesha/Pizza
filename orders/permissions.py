from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsDeliveredOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Grant the customer to read orders.
        if request.method in SAFE_METHODS:
            return True
        # If the order status is delivered customer must not be granted.
        return bool(False if obj.status == "delivered" else True)
