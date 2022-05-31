#April 28, 2022
#Ch 11 pg 480

#import the retail item class
from tkinter import Y
from retail_item_class import RetailItem

#create a cash register class
class CashRegister:
    def __init__(self,objects_list):
        self.objects_list = objects_list

    objects_list = []

    #define the purchase_item method
    def purchase_item(self,RetailItem):
        self.objects_list.append(RetailItem)

    #define the get_total method
    def get_total(self):
        total = 0
        for RetailItem in self.objects_list:
            total += RetailItem.get_price()
        return total
        
    #define the show_items method
    def show_items(self):
        for RetailItem in self.objects_list:
            print(RetailItem.get_item_desc())
            print(f'${RetailItem.get_price()}')
            print()
        
    #define the clear method
    def clear(self):
        self.objects_list = []

#test each funciton individually
# items_to_buy = CashRegister([])
# items_to_buy.purchase_item(retail_item_1)
# items_to_buy.purchase_item(retail_item_2)
# items_to_buy.show_items()
# print(items_to_buy.get_total())



#Cash Register class demonstration
#make a list of items for the user to choose from
retail_item_1 = RetailItem('bread','',4)
retail_item_2 = RetailItem('apple','',2)
retail_item_3 = RetailItem('avocado','',6)

print(retail_item_1.get_item_desc())
print(f'${retail_item_1.get_price()}')
print(retail_item_2.get_item_desc())
print(f'${retail_item_2.get_price()}')
print(retail_item_3.get_item_desc())
print(f'${retail_item_3.get_price()}')
#defint the main
def main():
    more_items = 'y'
    while more_items == 'y':
        item = input(print('Enter an item to buy (enter number)'))

        more_items = input(print('Would you like to buy another item?(y for yen n for no): '))





