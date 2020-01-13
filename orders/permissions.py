from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsDeliveredOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Grant the customer to read orders.
        if request.method in SAFE_METHODS:
            return True
        # If the order status is delivered customer must not be granted.
        return bool(False if obj.status == "delivered" else True)


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # All customers can read orders.
        # Only the owner of the order can update it.
        if request.method not in SAFE_METHODS:
            customer = request.data.get('customer')
            return bool(customer == obj.customer.id)
        return True
