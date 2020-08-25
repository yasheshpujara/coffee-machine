from setup import *

class TestBeverage:
    def test_brew(self, total_ingredients, stock_instance):
        stock_instance.add_stock(total_ingredients)
        for item, ingredients in beverages.items():
            beverage = Beverage(item, ingredients)
            assert beverage.brew() == item + " is prepared"