# python imports
import concurrent.futures

# project imports
from .stock import Stock
from .beverage import Beverage


class CoffeeMachine:
    """Coffee Machine that to serve different beverages.
    
    Args:
        outlets (int): number of outlets in machine that can serve beverage
        total_ingredients (dict): ingredients and their quantity available in the machine
    """
    def __init__(self, outlets: int, total_ingredients: dict):
        self.outlets = outlets
        self.stock = Stock.get_instance()
        self.stock.add_stock(total_ingredients)
    
    def serve(self, beverages: dict):
        """Serve beverages in parallel to customers.

        Args:
            beverages (dict): beverages with their required ingredients and quantity
        """
        servings = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.outlets) as executor:
            for item, ingredients in beverages.items():
                beverage = Beverage(item, ingredients)
                servings.append(executor.submit(beverage.brew))
            for serving in concurrent.futures.as_completed(servings):
                print(serving.result())
