import asyncio
from time import sleep
from inventory import Inventory
from catalogue import Catalogue

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


def build_combo():
    """ a function that helps to automatically build combo """
    pass

def cost_calculation():
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
    store_inventory = Inventory()
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