from rest_framework.serializers import ModelSerializer

from pizzas.models import Pizza, Flavor, Ingredient


class IngredientSerializer(ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('title',)


class FlavorSerializer(ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True, source='ingredients.all')

    class Meta:
        model = Flavor
        fields = ('title', 'ingredients',)


class PizzaSerializer(ModelSerializer):
    flavors = FlavorSerializer(many=True, read_only=True)

    class Meta:
        model = Pizza
        fields = ('title', 'size', 'pieces_number', 'flavors',)
