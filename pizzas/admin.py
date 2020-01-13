from django.contrib import admin

from pizzas.models import Pizza, Flavor, Ingredient

admin.site.register(Pizza)
admin.site.register(Flavor)
admin.site.register(Ingredient)
