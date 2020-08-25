# python imports
from typing import List, Dict

# project imports
from .stock import Stock

# considering time to prepare any beverage as 1 unit of time
TIME_TO_PREPARE = 1


class Beverage:
    """Beverage to be brewed in machine.
    
    Args:
        name (str): beverage name
        ingredients (Dict): ingredients to prepare beverage along with their quantity
    """
    def __init__(self, name: str, ingredients: Dict):
        self.name = name
        self.ingredients = ingredients

    def brew(self):
        """Brew the beverage. Beverage can be brewed if all ingredients with sufficient quantity are available.

        Returns:
            str: can beverage be brewed or not
        """

        stock = Stock.get_instance()

        # get unavailable ingredients from the current stock
        unavailable_ingredients = stock.use_ingredients(self.ingredients)

        # if any ingredient is not available then beverage can not be prepared and display the same
        if unavailable_ingredients:
            return self.name + " cannot be prepared because " + \
                ", ".join(unavailable_ingredients) + \
                    (" are" if len(unavailable_ingredients) > 1 else " is") + " not available"
        else:
            return self.name + " is prepared"
