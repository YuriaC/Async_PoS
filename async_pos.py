import asyncio
from catalogue import Catalogue

class Inventory:

    def __init__(self):
        self.inventory_contains = dict()
    
    async def get_number_of_items(self):
        """ An async method that returns the number of unique items in the restaurants catalogue """
        self.inventory_contains.count_item()
        item_num = self.inventory_contains.count
        return item_num
        
    async def get_catalogue(self):
        """ An async method that returns a dictionary containing the restaurant's catalogue """
        #return a dict obj containing the restaurant's catalogue
        pass


    async def get_stock(self, item_id):
        """ An Async method that returns the quantity of an item in the inventory based on its item_id """
        #return available quantity of item_id
        pass

    async def decrement_stock(item_id, count):
        """ An async method that decrements the count of an item in the inventory based on its item_id """
        pass

    async def get_item(item_id):
        """ An async method that returns the details abt a specific item based on its item_id """
        #return item detail
        pass