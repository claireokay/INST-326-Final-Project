"""A pizza simulation that outputs a summary of that days's inventory."""

# import statements
from argparse import ArgumentParser
from json import load
import sys
import re

TOPPINGS_INVENTORY= {
  'Olives': 10,
  'Sausages':2,
  'Mushrooms':10,  
  'Ham': 10,
  'Spinach':10,
  'Cheese':10,
  'Chicken':10,
  'Onions': 10,
}
pizzaSizeCosts= {"small": 5.99, "medium": 7.99, "large":9.99}
numToppingPrice={1:1, 2:2, 3:3, 4:4}
     
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
        # use key function to sort through to find inventory(ff)
        
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
        pattern(str): regular expression that filters through txt file 
        
    Side effects:
        prints out the customer customer name, pizza size, toppings, and price  
    """
    # open file
    with open(filepath, "r", encoding="utf-8") as f:

    # using regex to filter through list of customer and orders 
        pattern = r"""^(?P<Customer_Name>\w+),
        \s*(?P<Pizza_Size>[SML]),
        \s*(?P<Toppings>(?:\w+,?\s*)+),
        \s*\$(?P<Price>\d+\.\d{2})$"""
        for line in f: 
           match = re.match(pattern, line)
           if match:
               print(f"Customer: {match.group('Customer_Name')}")
               print(f"Pizza Size: {match.group('Pizza_Size')}")
               print(f"Toppings: {match.group('Toppings')}")
               print(f"Total Price: {match.group('Price')}")
           else:
              pass
    # use random module to choose random customers from list 

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