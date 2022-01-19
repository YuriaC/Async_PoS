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

def build_combo(lst):
    """ a function that helps to automatically build combo, returns a lst obj """
    burger_bin = []
    side_bin = []
    drink_bin = []
    
    for id in lst:
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
            break
    
    return combo

def print_combo(lst):
    """ a function to print combo info into appropriate format"""
    """use with build combo"""
    for dict_obj in lst:
        for price in dict_obj:  # price is the key for a dict_obj
            combo = dict_obj[price]
            print(f"{'{0:.2f}'.format(price)} Burger Combo:")
            for item in combo:
                if item["category"] == "Burgers":
                    print(f"{item['name']}") 
                    
                else:
                    print(f"{item['size']}{item['subcategory']}")

def cost_calculation():  # NOT IMPLEMENTED
    """ a function that helps to calculate the subtotal and tax of an order"""
    tax = None
    subtotal = None
    return (tax, subtotal)

def bool_user_input_validator(user_input, prompt):
    """ a function that helps to validate boolean user input"""
    while True:  # user input validation
        if user_input.lower() == "y":
            return True

        elif user_input.lower() == "N":
            # cancel order, restore stock
            return False

        else:
            print("Sorry but your input is invalid.")
            user_input = input(prompt)


def order_placement_helper(inv_obj):  # NEED MORE IMPLEMENTATION
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

        # and prodcut availability should be checked 
            
        elif item.lower() == "q":  # quitting ordering sequence
            print("Placing order...")
            break

        else:
            print("Please enter a valid number.")
            item = input("Enter an item number (q to quit): ")

    return user_selection


async def main():
    print("Welcome to the ProgrammingExpert Burger Bar @ Yuria brach!")
    print("Here is our menu: " )
    sleep(2)
    
    display_catalogue()

    order_placement_helper(store_inventory)  # function yet to be completed 

    build_combo()  # function yet to be implemented 

    (tax, subtotal) = cost_calculation()  # function yet to be implemented 
    total = tax + subtotal
    

    print("Here is your order summary: ")
    print(f"Subtotal: ${subtotal} \n Tax: ${tax} \n Total: ${total}")

    # order confirmation phase
    prompt = "Would you like to purchase this order for $12.92? (Y/N): "
    confirmation = input(prompt)  # order comfirmation 
    result = bool_user_input_validator(confirmation, prompt)
    if result:  # if user confirm order 
        print("Thank you for your order!")
        # proceed to confrim order 
        pass
    else:  
        print("No worries! We look forward to serve you again!")
        # proceed to cancel order and restore inventory stock
        pass

    
    prompt = "Would you like to make another order? (Y/N):"
    choice = input(prompt)
    result = bool_user_input_validator(choice, prompt)
    if result:
        order_placement_helper(store_inventory)
        # still need to implement combo making and price calculation and order comfirmation next
        # maybe use recursion?
    else: 
        print("Enjoy and have a good one!")

if __name__ == "__main__":
    asyncio.run(main())