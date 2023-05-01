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
    def __init__(self, pattern):
        self.pattern = pattern
        self.toppings = list()
        self.counter = 0
        self.revenue = 0
        self.pattern = r"""^(?P<Size>\w),
        \s*(?P<Topping1>[\w\s]+),
        ?\s*(?P<Topping2>[\w\s]+)?,
        ?\s*(?P<Topping3>[\w\s]+)?,
        ?\s*(?P<Topping4>[\w\s]+)?,?\s*([\w\s]+)?$
        """
        for line in self.pattern: 
           match = re.match(pattern, line)
           if match:
               self.size = match.group('Size')
               self.topping1 = match.group('Topping1')
               self.topping2 = match.group('Topping2')
               self.topping3 = match.group('Topping3')
               self.topping4 = match.group('Topping4')
               self.toppings.append(self.topping1)
               self.toppings.append(self.topping2)
               self.toppings.append(self.topping3)
               self.toppings.append(self.topping4)
           
           else:
              raise ValueError
    
    def getProfit(self):
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
        
    def getGross(self):
        
        """Calculate the gross revenue
       
        Returns
            grossProf (int): the gross profits.
        """
        self.revenue = 0
        for topping in self.toppings:
            self.counter += 1
        if self.size == "S":
            self.revenue += 5.99
        elif self.size == "M":
            self.revenue += 7.99
        else:
            revenue += 9.99
        self.revenue += self.counter+1  
        
        return self.revenue
            
               
    def __repr__(self):
            return f"Shop({self.pattern})"
    
    def __str__(self):
        return f""
        
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