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
    def __init__(self,filepath):
         
        self.inventory = TOPPINGS_INVENTORY 
        self.orders = {}
        self.order_num = 1
        pattern = r"""^(?P<Pizza_Size>[SML]),
            \s*(?P<Toppings>(?:\w+,?\s*)+)$"""
           
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f: 
                match = re.match(pattern,line)
                if match:
                    size = {match.group('Pizza_Size')}
                    Toppings = {match.group('Toppings').split(',')}
                    self.orders[self.order_num] = size, Toppings 
                    order_num +=1 
             
                else:
                    raise TypeError

    def getProfit(self):
        """Iterates through orders to determine the daily profit.
        
        Args:
            pizzaList (list): list of pizzas made.
        
        Returns:
            revenue (int): total revenue from the day's orders.
        """
        
        #counter that counts each topping and * by .25 (profit margin/topping)
        self.profit = 0 
        
        
    
    def updateInventory(self):
        """Updates invetory for the shop.
        
        Args:
            revenue (int): total revenue from the day's orders.
            inventory (dictionary): item string (key) to item list (value).
        
        Side effect:
            Update inventory dictionary.
        """
        
        for i in self.orders:
            topping_list =self.orders[i][1] 
            for j in topping_list:
                if j in self.inventory:
                    self.inventory[Topping]-=1
                
                

            
        
         
            
            
       
        # iterate through customers (dict) and keep track of each food used
        # iterate through inventory and subtract all foods used
        # use key function to sort through to find popular toppings (ff)
        
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