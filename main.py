from async_pos import Inventory
from time import sleep

def display_catalogue(catalogue):
    """ function that can output all the items in the catalogue """
    # the ids of items in the inventory will be the same as the item numbers that are displayed by this function
    pass

print("Welcome to the ProgrammingExpert Burger Bar @ Yuria brach!")
print("Here is our menu: " )
display_catalogue()

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


# process combo
# price calculation
# order comfirmation 
# order again?