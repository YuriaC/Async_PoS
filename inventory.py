import asyncio
import random
from catalogue import Catalogue 

class Inventory:

    def __init__(self):
        
        self.catalogue = Catalogue.catalogue
        self._generate_item_lookup_dict()  # initiate self.item attribute
        self.stock = {i + 1: random.randint(0, 15) for i in range(len(self.items))}  # randomly assign the stock for each item

    def _generate_item_lookup_dict(self):
        """ a class method that returns all the items in the catalogue as a dict obj within a bigger dict"""
        self.items = {}
        for category in self.catalogue:  # for keys in dict
            category_collection = self.catalogue[category]  # value = dict[key]

            if isinstance(category_collection, tuple):  # if value is tuple
                for item in category_collection:
                    new_item = item.copy()  # copy the dict obj
                    new_item["category"] = category  # insert new category key and value = category
                    new_item["subcategory"] = None   # insert new item has no subcategory
                    self.items[new_item["id"]] = new_item  # create a new item that in the new dict obj that can be accessed via the original id
            else:
                for subcategory in category_collection:  # for keys in subdict
                    for item in category_collection[subcategory]:  
                        new_item = item.copy()
                        new_item["category"] = category
                        new_item["subcategory"] = subcategory
                        self.items[new_item["id"]] = new_item
    
    def verify_item_id(func):
        """a decorator that serves to validate user input"""
        async def wrapper(self, val):
            if val not in self.stock:
                raise ValueError("Invalid item id!")
            
            else:
                result = await func(self, val)
                return result
            
        return wrapper

    async def get_number_of_items(self):
        """ An async method that returns the number of unique items in the restaurants catalogue """
        await asyncio.sleep(1)
        return len(self.items)
        
    async def get_catalogue(self):
        """ An async method that returns a dictionary containing the restaurant's catalogue """
        await asyncio.sleep(2)
        return self.catalogue

    @verify_item_id
    async def get_stock(self, item_id):
        """ An Async method that returns the quantity of an item in the inventory based on its item_id """
        current_stock = self.stock[item_id]
        await asyncio.sleep(2)
        return current_stock

    @verify_item_id
    async def decrement_stock(self, item_id, count = 1):
        """ An async method that decrements the count (default as 1) of an item in the inventory based on its item_id, returns bool type """
        current_stock = self.stock[item_id]
        await asyncio.sleep(1)
        if current_stock <= 0:
            return False
        
        else:
            self.stock[item_id] -= count
            return True
            
    @verify_item_id
    async def get_item(self, item_id):
        """ An async method that returns the details abt a specific item based on its item_id """
        await asyncio.sleep(1)
        return self.items[item_id]

    def __repr__(self):
        """ a method that alters the print out version of the Inventory class obj"""
        output = []
        for id in self.items:
            value = self.items[id]
            if value["category"] == "Burgers":
                str = f"{id}. {value['name']}  ${value['price']}; stock: {self.stock[id]}"
                output.append(str)
            
            else:
                str = f"{id}. {value['size']} {value['subcategory']}  ${value['price']}; stock: {self.stock[id]}"
                output.append(str)

        return "\n".join(output)
