from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    def test_init_sets_type_name_and_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)

        assert ingredient.type == INGREDIENT_TYPE_SAUCE
        assert ingredient.name == "hot sauce"
        assert ingredient.price == 100

    def test_get_price_returns_ingredient_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)

        assert ingredient.get_price() == 100

    def test_get_name_returns_ingredient_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)

        assert ingredient.get_name() == "hot sauce"

    def test_get_type_returns_ingredient_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)

        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE

    def test_get_filling_type_returns_filling_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)

        assert ingredient.get_type() == INGREDIENT_TYPE_FILLING