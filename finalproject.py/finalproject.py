"""A pizza simulation that outputs a summary of that days's inventory."""

# import statements
from argparse import ArgumentParser
import sys
import re

TOPPINGS_INVENTORY= {
  'olives': 10,
  'sausages':2,
  'mushrooms':10,  
  'ham': 10,
  'spinach':10,
  'cheese':10,
  'chicken':10,
  'onions': 10,
}
pizzaSizeCosts= {
"S": 5.99,
"M": 7.99, 
"L":9.99,
}
numToppingPrice={
    1:2, 
    2:3, 
    3:3, 
    4:4,
}
pizzaSizeRetail = {
"S": 2.00,
"M": 3.50,
"L": 4.00,   
}
    
class Shop:
    """Simulates the shop.
    
    Attributes:
        customers (dictionary): person string (key) to order list (value).
        inventory (dictionary): item string (key) to item list (value).
    """
    def __init__(self, customers, inventory, pattern):
        self.customers = customers
        self.inventory = inventory
        self.pattern = pattern
        
        self.pattern = r"""^(?P<Customer_Name>\w+),
        \s*(?P<Pizza_Size>[SML]),
        \s*(?P<Toppings>(?:\w+,?\s*)+)$"""
        for line in f: 
           match = re.match(pattern, line)
           if match:
               print(f"Customer: {match.group('Customer_Name')}")
               print(f"Pizza Size: {match.group('Pizza_Size')}")
             
           else:
              raise TypeError
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
    
    def getProfit(self, file):
        """Iterates through orders to determine the daily profit.
        
        Args:
            pizzaList (list): list of pizzas made.
        
        Returns:
            revenue (int): total revenue from the day's orders.
        """
        #counter that counts each topping and * by .25 (profit margin/topping)
     
        
    
    def updateInventory(self, revenue, inventory):"Fatma"
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
    """
    
    Args:
        pattern(str): regular expression that filters through txt file 
        
    Side effects:
        prints out the customer customer name, pizza size, toppings, and price  
    """
    # open file
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f: 
           match = re.match(,line)
           if match:
               print(f"Customer: {match.group('Customer_Name')}")
               print(f"Pizza Size: {match.group('Pizza_Size')}")
               print(f"Toppings: {match.group('Toppings')}")
             
           else:
              raise TypeError

# parse_args() function
def parse_args(arglist):
    """Andy: Parse command-line arguments.
    
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