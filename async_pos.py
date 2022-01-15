import asyncio

class Inventory:

    def __init__(self) -> None:
        pass
    
    async def get_number_of_items(self):
        """ An async method that returns the number of unique items in the restaurants catalogue """
        #return total_unique_items
        pass
 
    async def get_catalogue(self):
        """ An async method that returns a dictionary containing the restaurant's catalogue """
        #return a dict obj containing the restaurant's catalogue
        pass

    async def get_stock(self, item_id):
        """ An Async method that returns the quantity of an item in the inventory based on its item_id """
        #return available quantity of item_id
        pass

    async def decrement_stock(item_id, val):
        """ An async method that decrements the count of an item in the inventory based on its item_id """
        pass

    async def get_item(item_id):
        """ An async method that returns the details abt a specific item based on its item_id """
        #return item detail
        pass