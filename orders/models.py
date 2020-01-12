from django.db import models

from core.models import TimeStampedModel
from customers.models import Customer
from pizzas.models import Pizza


class Order(TimeStampedModel):
    STATUS_CHOICES = (
        ("shipped", "Shipped"),
        ("delivered", "Delivered"),
    )
    pizzas = models.ManyToManyField(to=Pizza)
    customer = models.ForeignKey(to=Customer, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    details = models.TextField(max_length=512, verbose_name="Order Details", null=True, blank=True)

    def __str__(self):
        return "{0} has ordered at {1}".format(self.customer, self.created.date())
