from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.viewsets import ModelViewSet

from orders.models import Order
from orders.permissions import IsDeliveredOrReadOnly, IsOwnerOrReadOnly
from orders.serializers import OrderListSerializer, OrderCreateSerializer


class OrderViewSet(ModelViewSet):
    """
    OrderViewSet for reading, writing, updating, delete orders.
    """
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('status', 'customer',)
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticatedOrReadOnly, IsDeliveredOrReadOnly, IsOwnerOrReadOnly)

    def create(self, request, *args, **kwargs):
        self.serializer_class = OrderCreateSerializer
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        self.serializer_class = OrderCreateSerializer
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
