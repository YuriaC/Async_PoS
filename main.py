import asyncio
from time import sleep
from async_pos import Inventory
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
    print("")


 
async def main():
    print("Welcome to the ProgrammingExpert Burger Bar @ Yuria brach!")
    print("Here is our menu: " )
    display_catalogue()
"""
    while True: 
        item = input("Please select an item by entering its item number (q to quit): ")
        # there should be no delay that causes that user to have to wait before adding another item to their order 
        if item.isdigit():
        # item number needs to be validated
        # and prodcut availability should be checked 
            pass

        elif item.lower() == "q":  # quitting ordering sequence
            print("Your order is: ")
            break

"""

if __name__ == "__main__":
    asyncio.run(main())



# process combo
# price calculation
# order comfirmation 
# order again?