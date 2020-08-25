from setup import *


class TestStock:
    def test_add_stock(self, stock_instance, total_ingredients):
        stock_instance.add_stock(total_ingredients)
        assert(stock_instance.stock == total_ingredients)

    def test_get_stock(self, stock_instance):
        assert type(stock_instance.stock) == dict, "Must return json for available ingredients"
        assert stock_instance.stock == stock_instance.original_stock

    @pytest.mark.parametrize("ingredients", beverage_ingredients)
    def test_use_ingredients(self, stock_instance, ingredients):
        assert len(stock_instance.use_ingredients(ingredients)) == 0

    def test_ingredients_running_low(self, stock_instance, total_ingredients):
        assert stock_instance.ingredients_running_low() == list(total_ingredients.keys())

    def test_refill_stock(self, stock_instance, total_ingredients):
        stock_instance.refill_stock(item="hot_water", quantity=1000)
        assert stock_instance.get_stock()["hot_water"] == 1000
        stock_instance.refill_stock(ingredients={"hot_milk": 500, "sugar_syrup": 100})
        assert stock_instance.get_stock()["hot_milk"] == 500
        assert stock_instance.get_stock()["sugar_syrup"] == 100
