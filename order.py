import asyncio
from inventory import Inventory

class Order:

    total_order = 0

    def __init__(self):
        self.order = []
        self.combo = []
        self.side_order = []
        self.total = 0

    async def order_placement_helper(self, inv_obj):
        """ a function that helps user to place an order"""
        tasks = []
        user_selection = []
        print("Please enter the number of items that you would like to add to your order. Enter q to complete your order.")
        while True:  # user input validation
            item = input("Enter an item number (q to end): ")
            if item.isdigit():
                item = int(item)

                if item < 1 or item > len(inv_obj.items):
                    print(f"Sorry, but {item} is not a valid item number.")
                
                else: 
                    task = asyncio.gather(inv_obj.decrement_stock(item), inv_obj.get_item(item))
                    tasks.append(task)
                    
            elif item.lower() == "q":  # quitting ordering sequence
                print("Placing order...")
                for task in tasks:
                    result = await task
                    user_selection.append(result)

                break

            else:
                print("Please enter a valid item number.")

        return user_selection

    def generate_order(self, user_selection):
        """a function that helps to generate order by getting detailed item info based on user selection"""
        
        if len(user_selection) == 0:
            self.order = None
        
        else: 
            for item in user_selection:
                if item[0]:  # if true
                    self.order.append(item[1])
                
                else:  # if there's no more of such item
                    print(f"Unfortunately item number {item[1]['id']} is out of stock and has been removed from your order. Sorry!")

        return self.order
        
    def build_combo(self):
        """ a function that helps to automatically build combo, returns a lst obj """

        def sort_method(dict):
            """ a local method for sorting lst"""
            return dict["price"]

        burger_bin = []
        side_bin = []
        drink_bin = []
        
        for item_detail in self.order:
            if item_detail["category"] == "Burgers":  # put burger in the burger_bin
                burger_bin.append(item_detail)
            
            elif item_detail["category"] == "Sides":  # put side item in the side_bin
                side_bin.append(item_detail)
            
            elif item_detail["category"] == "Drinks":
                drink_bin.append(item_detail)  # put drink in the drink_bin

        burger_bin.sort(key= sort_method)  # sort item bin by ascending price order
        side_bin.sort(key= sort_method)
        drink_bin.sort(key= sort_method)

        while True:
            if len(burger_bin) != 0 and len(side_bin) != 0 and len(drink_bin) != 0:
                lst = []  # to contain item info
                combo_dict = dict()  # to contain total price and all item info
                
                # gathering the most pricy items from each category
                lst.append(burger_bin.pop())
                lst.append(side_bin.pop())
                lst.append(drink_bin.pop())
                
                # calculating total price with a discount of 15%
                total_price = 0
                for item in lst:
                    total_price += item["price"]
                
                total_price = round(total_price * 0.75, 2)  # round the total price to the 100th decimal digit 
                
                # add total price as key and lst as value into a dict container
                combo_dict[total_price] = lst
                self.combo.append(combo_dict)  # add the dict obj into combo 
            
            else:
                self.side_order = burger_bin + side_bin + drink_bin
                break
        
        #return (self.combo, self.side_order)
    
    def print_summary(self):
        """ a function to print combo and other item into appropriate format. Also handels the cost calculation. 
        Return a floating point obj"""
        subtotal = 0
        # handeling price and printing of combos 
        for dict_obj in self.combo:
            for price in dict_obj:  # price is the key for a dict_obj
                subtotal += price   # calculating subtotal 
                # formatting and printing
                combo = dict_obj[price]
                print(f"\n${'{0:.2f}'.format(price)} Burger Combo:")
                for item in combo:
                    if item["category"] == "Burgers":
                        print(f"  {item['name']}") 
                        
                    else:
                        print(f"  {item['size']} {item['subcategory']}")
                print("")

        # handeling price and printing of single items 
        for dict_obj in self.side_order:
            subtotal += dict_obj["price"]  # calculating subtotal
            # handeling formatting and printing   
            if dict_obj["category"] == "Burgers":  
                print(f"${dict_obj['price']} {dict_obj['name']} ")
            
            else: 
                print(f"${dict_obj['price']} {dict_obj['size']} {dict_obj['subcategory']}")
        print("")

        tax = round(subtotal * 0.05, 2)
        self.total = tax + subtotal
        print(f"Subtotal: ${'{0:.2f}'.format(subtotal)} \nTax: ${'{0:.2f}'.format(tax)} \nTotal: ${'{0:.2f}'.format(self.total)}")
        
        return self.total 
    
    def place_order(self, confirmation, inv_obj):
        """ a function takes a bool type and a lst type. It serves to choose if or not to place order"""
        if confirmation:  # if true
            Order.total_order += 1
            print("Thank you for your order!")
        
        else:  # if false
            for item_id in self.order:
                inv_obj.stock[item_id["id"]] += 1  # restore stock
            
            print("No worries. We look forward to serve you again!")