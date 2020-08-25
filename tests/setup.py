import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
import pytest

from coffee_machine.stock import Stock
from coffee_machine.beverage import Beverage


test_input_config = json.load(open("./test.json", "r"))
beverages = test_input_config["machine"]["beverages"]
beverage_ingredients = beverages.values()


@pytest.fixture
def total_ingredients():
    return test_input_config["machine"]["total_items_quantity"] 

@pytest.fixture
def stock_instance():
    return Stock.get_instance()
