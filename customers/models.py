from django.db import models

from core.models import TimeStampedModel


class Customer(TimeStampedModel):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone = models.CharField(max_length=16, unique=True, help_text=u"Phone for driver contact")
    address = models.CharField(max_length=256)

    class Meta:
        ordering = ("first_name", "last_name",)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return u"{0} {1}".format(self.first_name, self.last_name)
