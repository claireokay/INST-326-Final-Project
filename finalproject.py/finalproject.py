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
    def __init__(self, filepath): 
        self.filepath = filepath
        self.inventory = TOPPINGS_INVENTORY 
        self.orders = {}
        self.order_num = 1
        self.total = 0
        pattern = r"^^(?P<Pizza_Size>[MLS]),\s*(?P<Toppings>(?:\w+,)*\w+)(?:,\s*)?$"
           
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f: 
                match = re.match(pattern,line)
                if match:
                    size = match.group('Pizza_Size')
                    Toppings = tuple(match.group('Toppings').split(','))
                    self.orders[self.order_num] = (size, Toppings) 
                    self.order_num +=1  
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
        

        for order in self.orders.values():
            p = pizzaSizeRetail[order[0]] + (0.25 * len(order[1])) if \
                (len(order[1]) > 0) else (p == pizzaSizeRetail[order[0]])
            self.total += p

        return self.total 
    
    def updateInventory(self):
        """Updates invetory for the shop.
        
        Args:
            revenue (int): total revenue from the day's orders.
            inventory (dictionary): item string (key) to item list (value).
        
        Side effect:
            Update inventory dictionary.
        """
        
        for order in self.orders.values():
            topping_list = order[1] 
            for j in topping_list:
                if j in self.inventory and self.inventory[j] > 1:
                    self.inventory[j]-=1
                else:
                    print(self.inventory)

                    
        return self.inventory
         
            
        # use key function to sort through to find popular toppings (ff)
    def get_popular_topping(self):
        """Returns the most popular topping from the list of orders
        
        Args: 
            self
            
        Return:
            A string representing the most popular topping  
        """    
        topping_counts = {}
        for order in self.orders.values():
            topping_list = order[1]
            for topping in topping_list:
                if topping in topping_counts:
                    topping_counts[topping] += 1
                else:
                    topping_counts[topping]=1
                    
        self.sorted_toppings = sorted(topping_counts.items(), key=lambda x: x[1], reverse=True)
        return self.sorted_toppings[0][0]        
    def getGross(self):
        
        """Calculate the gross revenue
       
        Returns
            grossProf (int): the gross profits.
        """
        self.revenue = 0
        for order in self.orders.values():
            topping_list = order[1]
            pizza_size= order[0]
            for item in topping_list:
                self.revenue += 1
            if pizza_size == "S":
                self.revenue += 5.99
            elif pizza_size == "M":
                self.revenue += 7.99
            else:
                self.revenue += 9.99
        self.revenue += self.order_num  
        self.revenue = round(self.revenue, 2)
        return self.revenue
            
               
    def __repr__(self):
            return f"Shop({self.filepath})"
    
    def __str__(self):
        return f"""Summary:
    Daily Revenue: ${self.revenue}
    Daily Profit: ${self.total}
    New Inventory: {self.inventory}
    Most Popular Toppings: {self.sorted_toppings}
    """
        
# main() function
def main(filepath): 
    """
    
    Args:
        pattern(str): regular expression that filters through txt file 
        
    Side effects:
        prints out the customer customer name, pizza size, toppings, and price  
    """
    newPizzaShop = Shop(filepath)
    newPizzaShop.getProfit()
    newPizzaShop.get_popular_topping()
    newPizzaShop.getGross()
    newPizzaShop.updateInventory()
    print(str(newPizzaShop))
    

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