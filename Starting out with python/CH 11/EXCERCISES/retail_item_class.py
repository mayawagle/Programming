#March 24
#Chapter 11 pg 480

#This program writes a class names RetailItem that holds the
#data about an item : item description, units in inventory and price
#it then creates 3 given retail item objects

#define the object
class RetailItem:
    def __init__(self,item_desc,units,price):
        self.__item_desc = item_desc
        self.__units = units
        self.__price = price
    
    #define the getters to later test the program
    def get_item_desc(self):
        return self.__item_desc

    def get_units(self):
        return self.__units

    def get_price(self):
        return self.__price

#PT 2 IN CLASS EX
    
