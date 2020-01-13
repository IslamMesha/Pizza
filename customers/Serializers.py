from rest_framework.serializers import ModelSerializer

from customers.models import Customer


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'email', 'phone', 'address',)
