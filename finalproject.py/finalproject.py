"""A pizza simulation that outputs a summary of that days's inventory."""

# import statements
import re
import argparse
import random

# pizza class
class Pizza:
    """Generates a customer's pizza.
     
    Attributes:
        crust (str): the customer's choice of pizza crust.
        sauce (str): the customer's choice of pizza sauce.
        size (str): the customer's choice of pizza size.
        toppings (list of str): the customer's choice of pizza toppings.
        
    Side effects:
        Sets attributes.
    """
    def __init__(self, crust, sauce, size = "medium"):
        self.crust = crust
        self.sauce = sauce
        self.size = size
        self.toppings = []
    
    def add_topping(self, topping):
        """Adds topping to pizza.
        
        Attributes:
            topping (str): the topping to be added.
            
        Side effects:
            topping (list of str): receives a topping.
        """
        self.toppings.append(topping)

# customer class
class Customer:
    """Generates class for each customer.
    
    Attributes:
        order (int): the customer's order number.
        
    Side effects:
        Sets attributes.
    """
    def __init__(self, order):
        self.order = order
        
    def makeOrder(self):
        pass
  
# shop class      
class Shop:
    """Simulates the shop.
    
    Attributes:
    
    Side effects:
    
    """
    def __init__(self, ):
        pass
    
    def orderQueue(self):
        # pass in text file of customers and their orders
        pass
    
# main() function
def main(filepath):
    """
    """
    
    with open(filepath, "r", encoding="utf-8") as f:
        orders = load(f)
        
    dailySummary = Shop(orders)

# parse_args() function

# if __name__ = "__main__": statement