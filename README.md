# Coffee Machine
----------------

A simple coffee machine that dispenses drinks. It has the following properties.

### Properties
1. It will be serving some beverages.
2. Each beverage will be made using some ingredients.
3. Assume time to prepare a beverage is the same for all cases.
4. The quantity of ingredients used for each beverage can vary. Also, the same ingredient (ex:water) can be used for multiple beverages.
5. There would be ​N​​( N is an integer )​ outlet from which beverages can be served.For N = 2 [ 2 outlets in a machine ]For N = 3 [ 3 outlets in a machine ]
6. Maximum ​N​ beverages can be served in ​parallel​.
7. Any beverage can be served only if all the ingredients are available in terms of quantity.
8. There would be an indicator that would show which all ingredients are running low. There should some methods to refill them.

### Usage
* The input will be taken from `resources/input.json`.
* Run `python3 main.py` to dispense drinks.

### Output
* Display result to stdout. Following is the example output.
```
hot_coffee is prepared
hot_tea is prepared
black_tea cannot be prepared because hot_water, sugar_syrup are not available
green_tea cannot be prepared because sugar_syrup, green_mixture are not available
```