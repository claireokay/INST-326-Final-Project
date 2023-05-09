"""A pizza simulation that outputs a summary of that days's inventory."""
from argparse import ArgumentParser
import sys
import re
import matplotlib.pyplot as plt

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
    """_summary_
    """    
    def __init__(self, filepath):
        """Reads a text file containing all of the customer orders for a 
        particular day 

        Args:
            filepath (str): a text file that contains customer information 
            including the size of pizza and the toppings on the pizza

        Raises:
            TypeError: when the 
        """        
        self.filepath = filepath
        self.inventory = TOPPINGS_INVENTORY 
        self.orders = {}
        self.order_num = 1
        self.total = 0
        pattern = r"""(?x)^(?P<Pizza_Size>[MLS]),\s*(?P<Toppings>(?:\w+,)*\w+)
        (?:,\s*)?$"""
           
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
        return self.inventory
         
         
    def get_popular_topping(self):
        """Returns the most popular topping from the list of orders
            
        Returns:
            self.sorted_toppings (list of tuples)
        """    
        topping_counts = {}
        for order in self.orders.values():
            topping_list = order[1]
            for topping in topping_list:
                if topping in topping_counts:
                    topping_counts[topping] += 1
                else:
                    topping_counts[topping]=1
                    
        self.sorted_toppings = sorted(topping_counts.items(), key=lambda x: 
            x[1], reverse=True)
        return self.sorted_toppings[0][0] 
    
           
    def getGross(self):
        """Calculates the gross revenue of the Pizza Shop for a particular day.

        Returns:
            self.revenue (float): _description_
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


def main(filepath, path1, path2=None, path3=None, path4=None, path5=None,
         path6=None): 
    """Instantiates the Shop class for up to 7 different days of operation and
    runs all methods within the class. If there is 

    Args:
        filepath (_type_): _description_
        path1 (_type_): _description_
        path2 (_type_, optional): _description_. Defaults to None.
        path3 (_type_, optional): _description_. Defaults to None.
        path4 (_type_, optional): _description_. Defaults to None.
        path5 (_type_, optional): _description_. Defaults to None.
        path6 (_type_, optional): _description_. Defaults to None.
    
    Side Effects:
        Writes to stdout.
    """    
    newPizzaShop = Shop(filepath)
    dailyprofit = newPizzaShop.getProfit()
    newPizzaShop.get_popular_topping()
    newPizzaShop.getGross()
    newPizzaShop.updateInventory()
    print(str(newPizzaShop))
    if path1 is not None:
        newPizzaShop1 = Shop(path1)
        dailyprofit1 = newPizzaShop1.getProfit()
        newPizzaShop1.get_popular_topping()
        newPizzaShop1.getGross()
        newPizzaShop1.updateInventory()
        print(str(newPizzaShop1))
    if path2 is not None:
        newPizzaShop2 = Shop(path2)
        dailyprofit2 = newPizzaShop2.getProfit()
        newPizzaShop2.get_popular_topping()
        newPizzaShop2.getGross()
        newPizzaShop2.updateInventory()
        print(str(newPizzaShop2))
    if path3 is not None:
        newPizzaShop3 = Shop(path3)
        dailyprofit3 = newPizzaShop3.getProfit()
        newPizzaShop3.get_popular_topping()
        newPizzaShop3.getGross()
        newPizzaShop3.updateInventory()
        print(str(newPizzaShop3))
    if path4 is not None:
        newPizzaShop4 = Shop(path4)
        dailyprofit4 = newPizzaShop4.getProfit()
        newPizzaShop4.get_popular_topping()
        newPizzaShop4.getGross()
        newPizzaShop4.updateInventory()
        print(str(newPizzaShop4))
    if path5 is not None:
        newPizzaShop5 = Shop(path5)
        dailyprofit5 = newPizzaShop5.getProfit()
        newPizzaShop5.get_popular_topping()
        newPizzaShop5.getGross()
        newPizzaShop5.updateInventory()
        print(str(newPizzaShop5))
    if path6 is not None:
        newPizzaShop6 = Shop(path6)
        dailyprofit6 = newPizzaShop6.getProfit()
        newPizzaShop6.get_popular_topping()
        newPizzaShop6.getGross()
        newPizzaShop6.updateInventory()
        print(str(newPizzaShop6))
    if (path1 is not None and path2 is not None and path3 is not None and
        path4 is not None and path5 is not None and path6 is not None):
        profitlist= [dailyprofit, dailyprofit1, dailyprofit2, dailyprofit3, 
                 dailyprofit4, dailyprofit5, dailyprofit6]
        plt.plot(profitlist)
        plt.xlabel('Days')
        plt.ylabel('Profit in Dollars')
        plt.title("Pizza Shop Profit over 7 days")
        plt.show()   

# parse_args() function
def parse_args(arglist):
    """_summary_

    Args:
        arglist (_type_): _description_

    Returns:
        _type_: _description_
    """    
    parser = ArgumentParser()
    parser.add_argument("filepath", help="path to text file")
    parser.add_argument("-path1", "--path1", type=str, default=None,
                        help="path for a new text file of a new day")
    parser.add_argument("-path2", "--path2", type=str, default=None,
                        help="path for a new text file of a new day")
    parser.add_argument("-path3", "--path3", type=str, default=None,
                        help="path for a new text file of a new day")
    parser.add_argument("-path4", "--path4", type=str, default=None,
                        help="path for a new text file of a new day")
    parser.add_argument("-path5", "--path5", type=str, default=None,
                        help="path for a new text file of a new day")
    parser.add_argument("-path6", "--path6", type=str, default=None,
                        help="path for a new text file of a new day")
    return parser.parse_args(arglist)

# if __name__ = "__main__": statement
if __name__ == "__main__":
    try:
        args = parse_args(sys.argv[1:])
    except ValueError as e:
        sys.exit(str(e))
    main(args.filepath, args.path1, args.path2, args.path3, args.path4, 
         args.path5, args.path6)