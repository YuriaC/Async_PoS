import asyncio
from time import sleep
from inventory import Inventory
from catalogue import Catalogue

store_inventory = Inventory()

def display_catalogue():
    """ function that can output all the items in the catalogue """
    # the ids of items in the inventory will be the same as the item numbers that are displayed by this function
    
    print("--------- Burgers ----------- \n")
    item_collection = Catalogue.catalogue["Burgers"]
    for item in item_collection: 
        print(f'{item["id"]}. {item["name"]} ${item["price"]}')
    print("")

    print("---------- Sides ------------ \n")
    for subcategory in Catalogue.catalogue["Sides"]:
        print(f"{subcategory}")
        item_collection = Catalogue.catalogue["Sides"][subcategory]
        for item in item_collection: 
            print(f'{item["id"]}. {item["size"]} ${item["price"]}')
        print("")
    print("")


    print("---------- Drinks ------------ \n")
    for subcategory in Catalogue.catalogue["Drinks"]:
        print(f"{subcategory}")
        item_collection = Catalogue.catalogue["Drinks"][subcategory]
        for item in item_collection: 
            print(f'{item["id"]}. {item["size"]} ${item["price"]}')
        print("")
    
    print("------------------------------")

def order_placement_helper(inv_obj):
    """ a function that helps user to place an order"""
    user_selection = []
    print("Please enter the number of items that you would like to add to your order. Enter q to complete your order.")
    while True:  # user input validation
        item = input("Enter an item number (q to end): ")
        if item.isdigit():
            item = int(item)

            if item < 1 or item > len(inv_obj.items):
                print(f"Sorry, but {item} is not a valid item number.")
                item = input("Enter an item number (q to end): ")
            
            else: 
                user_selection.append(item)
            
        elif item.lower() == "q":  # quitting ordering sequence
            print("Placing order...")
            break

        else:
            print("Please enter a valid number.")
            item = input("Enter an item number (q to quit): ")

    return user_selection

def generate_order(user_selection):
    """a function that helps to generate order by getting detailed item info based on user selection"""
    order = []
    if len(user_selection) == 0:
        return None
    
    else: 
        for item_id in user_selection:
            stock_check = store_inventory.decrement_stock(item_id)  # returns bool type

            if stock_check:  # if true
                order.append(store_inventory.get_item(item_id))
            
            else:  # if there's no more of such item
                print(f"Unfortunately item number {item_id} is out of stock and has been removed from your order. Sorry!")

        return order

def build_combo(order):
    """ a function that helps to automatically build combo, returns a lst obj """
    burger_bin = []
    side_bin = []
    drink_bin = []
    
    for id in order:
        item_detail = store_inventory.get_item(id)
        if item_detail["category"] == "Burgers":  # put burger in the burger_bin
            burger_bin.append(item_detail)
        
        elif item_detail["category"] == "Sides":  # put side item in the side_bin
            side_bin.append(item_detail)
        
        elif item_detail["category"] == "Drinks":
            drink_bin.append(item_detail)  # put drink in the drink_bin
    
        def sort_method(dict):
            """ a local method for sorting lst"""
            return dict["price"]

    burger_bin.sort(key= sort_method)  # sort item bin by ascending price order
    side_bin.sort(key= sort_method)
    drink_bin.sort(key= sort_method)

    combo = []
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
            combo.append(combo_dict)  # add the dict obj into combo 
        
        else:
            other_order = burger_bin + side_bin + drink_bin
            break
    
    return (combo, other_order)

def print_summary(lst, lst2):
    """ a function to print combo and other item into appropriate format. Also handels the cost calculation. 
    Return a floating point obj"""
    subtotal = 0
    # handeling price and printing of combos 
    for dict_obj in lst:
        for price in dict_obj:  # price is the key for a dict_obj
            subtotal += price   # calculating subtotal 
            # formatting and printing
            combo = dict_obj[price]
            print(f"{'{0:.2f}'.format(price)} Burger Combo:")
            for item in combo:
                if item["category"] == "Burgers":
                    print(f"{item['name']}") 
                    
                else:
                    print(f"{item['size']}{item['subcategory']}")

    # handeling price and printing of single items 
    for dict_obj in lst2:
        subtotal += item["price"]  # calculating subtotal
        # handeling formatting and printing   
        if dict_obj["category"] == "Burgers":  
            print(f"${dict_obj['price']} {dict_obj['name']} ")
        
        else: 
            print(f"${dict_obj['price']} {item['size']} {item['subcategory']}")

    tax = round(subtotal * 0.05, 2)
    total = tax + subtotal
    print(f"Subtotal: ${'{0:.2f}'.format(subtotal)} \nTax: ${'{0:.2f}'.format(tax)} \nTotal: ${'{0:.2f}'.format(total)}")
    
    return total 

def bool_user_input_validator(user_input, prompt):
    """ a function that helps to validate boolean user input"""
    while True:
        if user_input.lower() == "y":
            return True

        elif user_input.lower() == "N":
            return False

        else:
            print("Sorry but your input is invalid.")
            user_input = input(prompt)

def place_order(confirmation, order):
    """ a function takes a bool type and a lst type. It serves to choose if or not to place order"""
    if confirmation:  # if true
        print("Thank you for your order!")
    
    else:  # if false
        for item_id in order:
            store_inventory.stock[item_id] += 1  # restore stock
        
        order.clear()
        print("No worries. We look forward to serve you again!")


async def main():
    print("Welcome to the ProgrammingExpert Burger Bar @ Yuria brach!")
    print("Here is our menu: " )
    sleep(2)  # mimic loading 
    display_catalogue()  # show menu

    while True:
        user_selection = order_placement_helper(store_inventory)
        print("Placing order...")
        
        if len(user_selection) != 0:  # if user selected any items
            # order processing phase
            order = generate_order(user_selection)  # retrive item detail and checking stock
            (combo, other_order) = build_combo(order)  # generating combo outta all items
            total = print_summary(combo, other_order)  # handeling printing and fees 

            # order confirmation phase
            prompt = f"Would you like to purchase this order for ${total}? (Y/N): "
            confirmation = input(prompt)  # order comfirmation 
            result = bool_user_input_validator(confirmation, prompt)
            
            # finalizing interaction phase
            place_order(result, order)

        
        prompt = "Would you like to make another order? (Y/N):"
        choice = input(prompt)
        result = bool_user_input_validator(choice, prompt)
        if not result:  # if user don't wish to make another order
            print("Enjoy and have a good one!")
            break  # break out of while loop


if __name__ == "__main__":
    asyncio.run(main())