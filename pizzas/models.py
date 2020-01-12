from django.db import models

from core.models import TimeStampedModel


class Ingredient(TimeStampedModel):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class Flavor(TimeStampedModel):
    title = models.CharField(max_length=256)
    ingredients = models.ManyToManyField(to=Ingredient)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("title",)


class Pizza(TimeStampedModel):
    SIZE_CHOICES = (
        ("small", "Small"),
        ("medium", "Medium"),
        ("large", "Large"),
    )
    title = models.CharField(max_length=256, null=True, blank=True)
    size = models.CharField(max_length=20, choices=SIZE_CHOICES, default="small")
    pieces_number = models.PositiveSmallIntegerField(default=8)
    flavors = models.ManyToManyField(to=Flavor)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("title",)
