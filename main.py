import asyncio
from time import sleep
from catalogue import Catalogue
from inventory import Inventory
from order import Order

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

    print("---------- Drinks ------------ \n")
    for subcategory in Catalogue.catalogue["Drinks"]:
        print(f"{subcategory}")
        item_collection = Catalogue.catalogue["Drinks"][subcategory]
        for item in item_collection: 
            print(f'{item["id"]}. {item["size"]} ${item["price"]}')
        print("")
    
    print("------------------------------")

def bool_user_input_validator(user_input, prompt):
    """ a function that helps to validate boolean user input"""
    while True:
        if user_input.lower() == "y":
            return True

        elif user_input.lower() == "n":
            return False

        else:
            print("Sorry but your input is invalid.")
            user_input = input(prompt)

async def main():
    print("Welcome to the ProgrammingExpert Burger Bar @ Yuria brach!")
    print("Here is our menu: " )
    sleep(1.5)  # mimic loading 
    display_catalogue()  # show menu

    while True:
        new_order = Order()
        task = asyncio.create_task(new_order.order_placement_helper(store_inventory))
        user_selection = await task
        
        if len(user_selection) != 0:  # if user selected any items
            # order processing phase     
            new_order.generate_order(user_selection)  # retrive item detail and checking stock
            new_order.build_combo()  # generating combo outta all items within order
            total = round(new_order.print_summary(), 2)  # handeling printing and fees 

            # order confirmation phase
            prompt = f"Would you like to purchase this order for ${total}? (Y/N): "
            confirmation = input(prompt)  # order comfirmation 
            result = bool_user_input_validator(confirmation, prompt)
            
            # finalizing interaction phase
            new_order.place_order(result, store_inventory)

        
        prompt = "Would you like to make another order? (Y/N):"
        choice = input(prompt)
        result = bool_user_input_validator(choice, prompt)
        if not result:  # if user don't wish to make another order
            print("Thank you for visiting! Wish you have a good one.")
            break  # break out of while loop


if __name__ == "__main__":
    asyncio.run(main())