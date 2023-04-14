"""A pizza simulation that outputs a summary of that days's inventory."""

# import statements
from argparse import ArgumentParser
from json import load
import sys
import re
import random

pizzaSizeCosts= {"small": 5.99, "medium": 7.99, "large":9.99}
numToppingPrice={1:1, 2:2, 3:3, 4:4}

# pizza class
class Pizza:
    """Generates a customer's pizza.
     
    Attributes:
        crust (str): the customer's choice of pizza crust.
        sauce (str): the customer's choice of pizza sauce.
        size (str): the customer's choice of pizza size.
        toppings (list of str): the customer's choice of pizza toppings.
    """
    def __init__(self, crust, sauce, size = "medium"):
        """Sets attributes to Pizza class.
        
        Args:
            crust (str): the customer's choice of pizza crust.
            sauce (str): the customer's choice of pizza sauce.
            size (str): the customer's choice of pizza size.
            toppings (list of str): the customer's choice of pizza toppings.
        
        Side effects:
            Sets arguments.
        """
        self.crust = crust
        self.sauce = sauce
        self.size = size
        self.toppings = []
    
    def add_topping(self, topping):
        """Adds topping to pizza.
        
        Args:
            topping (str): the topping to be added.
            
        Side effects:
            topping (list of str): receives a topping.
        """
        self.toppings.append(topping)


# shop class      
class Shop:
    """Simulates the shop.
    
    Attributes:
        customers (dictionary): person string (key) to order list (value).
        inventory (dictionary): item string (key) to item list (value).
    """
    def __init__(self, customers, inventory):
        self.customers = customers
        self.inventory = inventory
        
    def makeOrders(self, customers):
        """Makes order for a customer's pizzas.
        
        Args:
            customers (dictionary): person string (key) to order list (value).
        
        Returns:
            pizzaList (list): list of pizzas made.
        """
        # iterate through each customer
        for customer, pizza in customers.items():
            # call Pizza on each pizza in the list
            # append the pizzas to the list
            pass
    
    def getProfit(self, pizzaList):
         """Iterates through orders to determine the daily profit.
        
        Args:
            pizzaList (list): list of pizzas made.
        
        Returns:
            revenue (int): total revenue from the day's orders.
        """
        # iterate through customers (dict)
        # call Customer on each iteraction
            # Customer will generate an order
        # orderQueue will return the total profits (int)
    
    def updateInventory(self, revenue, inventory):
         """Updates invetory for the shop.
        
        Args:
            revenue (int): total revenue from the day's orders.
            inventory (dictionary): item string (key) to item list (value).
        
        Side effect:
            Update inventory dictionary.
        """
        # iterate through customers (dict) and keep track of each food used
        # iterate through inventory and subtract all foods used
        
    def getGross(self, revenue, inventory):
        """Calculate the gross revenue
        
        Args:
            revenue (int): total revenue from the day's orders.
            inventory (dictionary): item string (key) to item list (value).
        
        Returns
            grossProf (int): the gross profits.
        """
    def __repr__(self):
            return f"Shop({self.customers}, {self.inventory})"
    
# main() function
def main(filepath):
    """--
    
    Args:
        --
        
    Side effects:
        Prints results to stdout.
    """
    # open file
    with open(filepath, "r", encoding="utf-8") as f:
        orders = load(f)
    
    # create Shop class, pass in inventory and customers??
    dailySummary = Shop(orders)
    
    # print results

# parse_args() function
def parse_args(arglist):
    """Parse command-line arguments.
    
    Expect one mandatory argument:
        filepath: a path to file containing --.
    
    Args:
        arglist (list of str): argument from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("filepath", help="path to text file")
    # we might need a second argument
    return parser.parse_args(arglist)

# if __name__ = "__main__": statement
if __name__ == "__main__":
    try:
        args = parse_args(sys.argv[1:])
    except ValueError as e:
        sys.exit(str(e))
    main(args.filepath)