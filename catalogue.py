class Catalogue:

    burgers = {    
        1 : ("Python Burger", 5.99),
        2 : ("C Burger", 4.99),     
        3 : ("Ruby Burger", 6.49),
        4 : ("Go Burger", 5.99),
        5 : ("C++ Burger", 7.99),
        6 : ("Java Burger", 7.99)
    }

    sides = {
        
        "Fries" : {
            7 : ("Small", 2.49),
            8 : ("Medium", 3.49),     
            9 : ("Large", 4.29)
        },
        
        # Caesar Salad 
        "Caesar Salad" : {
            10 : ("Small", 3.49),     
            11 : ("Large", 4.49)
        },
    }
    

    drinks = {
        "Coke" : {
            12 : ("Small Coke", 1.99),
            13 : ("Medium Coke", 2.49),     
            14 : ("Large Coke", 2.99)
        },


        "Chocolate Milk Shake" : {
            15 : ("Small", 1.99),     
            16 : ("Medium", 2.49),
            17 : ("Large", 2.99)
        },


        "Chocolate Milk Shake" : {
            18 : ("Small", 1.99),     
            19 : ("Medium", 2.49),
            20 : ("Large", 2.99)
        }

    }

    def __init__(self):
        self.count = 0
    
    def count_item(self):
        """ a method for returning total number of unique item within the catalogue"""
        total_item_num = len(self.burgers) + len(self.sides) + len(self.drinks)
        self.count = total_item_num

    def __repr__(self):
        """ a method for printing the catalogue object"""
        print("--------- Burgers ----------- \n")
        for key, tup in self.burgers.items():
            print(f"{key}. {tup[0]} ${tup[1]}")
        print("")

        print("---------- Sides ------------ \n")
        for key, dict in self.sides.items():
            print(f"{key}:") 
            for dict_key, dict_tup in dict.items():
                print(f"{dict_key}. {dict_tup[0]} ${dict_tup[1]}")
            print("")
        print("")

        print("---------- Drinks ------------ \n")
        for key, dict in self.sides.items():
            print(f"{key}:") 
            for dict_key, dict_tup in dict.items():
                print(f"{dict_key}. {dict_tup[0]} ${dict_tup[1]}")
            print("")   
        print("")


    def add_item(self, category, name, price):
        pass  # for later implementation maybe switch to linked list data structure

