from rest_framework.fields import SerializerMethodField, ChoiceField
from rest_framework.serializers import ModelSerializer

from customers.Serializers import CustomerSerializer
from orders.models import Order
from pizzas.serializers import PizzaSerializer


class OrderListSerializer(ModelSerializer):
    pizzas_number = SerializerMethodField()
    customer = CustomerSerializer(read_only=True)
    status = ChoiceField(choices=Order.STATUS_CHOICES, read_only=True)
    pizzas = PizzaSerializer(many=True, read_only=True, source='pizzas.all')

    @staticmethod
    def get_pizzas_number(obj):
        return obj.pizzas.count()

    class Meta:
        model = Order
        ordering = ('-created',)
        fields = ('id', 'pizzas', 'customer', 'status', 'details', 'pizzas_number')


class OrderCreateSerializer(ModelSerializer):

    # def create(self, validated_data):
    #     order = Order.objects.create(**validated_data)
    #     return order

    def update(self, instance, validated_data):
        pizzas = validated_data.pop('pizzas', [])
        instance.status = validated_data.get('status', instance.status)
        instance.details = validated_data.get('details', instance.details)
        instance.customer = validated_data.get('customer', instance.customer)
        instance.pizzas.set(pizzas)
        return instance

    class Meta:
        model = Order
        ordering = ('-created',)
        fields = ('id', 'pizzas', 'customer', 'status', 'details',)
