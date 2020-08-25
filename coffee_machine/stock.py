from typing import Dict, List
from collections import defaultdict
from threading import Lock
import threading

INGREDIENT_LOW_THRESHOLD = 0.1

class Stock:
    __instance = None

    @staticmethod
    def get_instance():
        """Static access method.

        Returns:
            object: Stock instance
        """
        if Stock.__instance is None:
            Stock()
        return Stock.__instance

    def __init__(self):
        """Virtual private constructor

        Raises:
            Exception: can only be accessed by static method
        """
        if Stock.__instance is not None:
            raise Exception("Stock is a singleton class. Get Stock instance by Stock.get_instance(ingredients).")
        Stock.__instance = self
        self.lock = Lock()
    
    def add_stock(self, ingredients: Dict):
        """Add ingredients along with their quantity to stock.

        Args:
            ingredients (Dict): ingredients list with their quantity
        """
        self.original_stock = ingredients
        self.stock = self.original_stock.copy()

    def get_stock(self) -> Dict:
        """Get current stock.

        Returns:
            Dict: current ingredients with their quantity
        """
        return self.stock

    def use_ingredients(self, ingredients_needed: Dict) -> List[str]:
        """Check availability of ingredients present in the machine to make beverage.
        Use up the ingrdients if all are available.
        Checking the ingredient stock is thread safe.
        So, if ingredients are not available for beverage,
        then it will return the list of such ingredients.

        Args:
            ingredients_needed (Dict): ingredients needed to make a beverage

        Returns:
            List[str]: unavailable ingredients
        """
        with self.lock:
            unavailable_ingredients = []

            # check if all ingredients are available to make beverage
            for ingredient, quantity in ingredients_needed.items():
                if ingredient not in self.stock or quantity > self.stock[ingredient]:
                    unavailable_ingredients.append(ingredient)
            
            # use ingredients only if all are available in sufficient quantity
            if not unavailable_ingredients:
                for ingredient, quantity in ingredients_needed.items():
                    self.stock[ingredient] -= quantity

        return unavailable_ingredients

    def refill_stock(self, item: str="", quantity: int=0, ingredients: Dict={}):
        """Refill the ingredients individually or by multiple at once.

        Args:
            item (str, optional): ingredient name. Defaults to "".
            quantity (int, optional): ingredient quantity. Defaults to 0.
            ingredients (Dict, optional): ingredients json with their quantity. Defaults to {}.
        """
        if item != "":
            self.stock[item] += quantity
        elif ingredients:
            for item, quantity in ingredients.items():
                if item not in self.stock:
                    print(f"Skipping {item}, as it is not part of coffee machine.")
                    continue
                self.stock[item] += quantity
        else:
            print("No ingredients provided to refill.")
    
    def ingredients_running_low(self) -> List[str]:
        """Get the ingredients which are running low based on the threshold.
        Threshold is 10%.

        Returns:
            List[str]: ingredients less than acceptable threshold
        """
        low_ingredients = list()
        for current, original in zip(self.stock.items(), self.original_stock.items()):
            if current[1] / original[1] <= INGREDIENT_LOW_THRESHOLD:
                low_ingredients.append(current[0])
        return low_ingredients
