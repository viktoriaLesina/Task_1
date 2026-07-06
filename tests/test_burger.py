from burger import Burger
from bun import Bun
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:

    def test_init_creates_empty_burger(self):
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns_sets_bun(self):
        burger = Burger()
        bun = Bun("black bun", 100)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient_adds_ingredient_to_list(self):
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]

    def test_remove_ingredient_removes_ingredient_from_list(self):
        burger = Burger()
        ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        burger.add_ingredient(ingredient1)
        ingredient2 = Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 101.1)
        burger.add_ingredient(ingredient2)
        burger.remove_ingredient(1)
        assert burger.ingredients == [ingredient1]

    def test_move_ingredient_moves_ingredient_to_new_position(self):
        burger = Burger()
        ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        burger.add_ingredient(ingredient1)
        ingredient2 = Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 101.1)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(1, 0)
        assert burger.ingredients == [ingredient2, ingredient1]

    def test_get_price_returns_total_price(self):
        burger = Burger()
        bun = Bun("black bun", 100)
        burger.set_buns(bun)
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        burger.add_ingredient(ingredient)
        expected_price = bun.get_price() * 2 + ingredient.get_price()

        assert burger.get_price() == expected_price




    def test_get_receipt_returns_receipt_with_bun_ingredient_and_price(self):
        burger = Burger()
        bun = Bun("black bun", 100)
        burger.set_buns(bun)
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        burger.add_ingredient(ingredient)
        receipt = burger.get_receipt()
        assert bun.get_name() in receipt
        assert ingredient.get_name() in receipt
        assert str(burger.get_price()) in receipt