import json

from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.reverse import reverse

from customers.models import Customer
from orders.models import Order
from pizzas.models import Pizza


class OrderAPITests(TestCase):
    list_create_url = reverse('orders-list')
    read_update_delete_url = reverse('orders-detail', kwargs={"pk": "1"})

    def setUp(self):
        pizza, created = Pizza.objects.get_or_create(size='small')
        customer, created = Customer.objects.get_or_create(first_name='Islam')

        order_dict = {
            "status": "shipped",
            "customer": customer,
            "status": "shipped",
            "details": "This order for testing...",
        }

        for i in range(4):
            order = Order.objects.create(**order_dict)
            order.pizzas.add(pizza)

    def test_list(self):
        response = self.client.get(self.list_create_url)
        self.assertEquals(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEquals(len(data), 4)

    def test_detail(self):
        response = self.client.get(self.read_update_delete_url)
        self.assertEquals(response.status_code, 200)
        data = json.loads(response.content)

        # Six fields for the order.
        self.assertEquals(len(data), 6)

    def test_create(self):
        order = {"pizzas": [1], "customer": 1, "status": "shipped", "details": "A small size pizza for me. Hmm.."}
        user, created = User.objects.get_or_create(username__icontains="islam")
        self.client.force_login(user=user)
        response = self.client.post(self.list_create_url, order)
        data = json.loads(response.content)
        data.pop("id")
        self.assertEquals(response.status_code, 201)
        content = {"pizzas": [1], "customer": 1, "status": "shipped", "details": "A small size pizza for me. Hmm.."}
        self.assertEquals(data, content)
        self.assertEquals(Order.objects.count(), 5)

    def test_delete(self):
        user, created = User.objects.get_or_create(username__icontains="islam")
        self.client.force_login(user=user)
        data = json.dumps({"customer": 1})
        response = self.client.delete(self.read_update_delete_url, data, content_type="application/json")
        self.assertEquals(response.status_code, 204)
        self.assertEquals(Order.objects.count(), 3)
