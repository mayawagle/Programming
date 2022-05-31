#March 24
#Chapter 11 pg 480

#This program writes a class names RetailItem that holds the
#data about an item : item description, units in inventory and price
#it then creates 3 given retail item objects

#import the class from its module
import retail_item_class

#define the main
def main():
    #define the items
    item_1 = retail_item_class.RetailItem('Jacket', 12, 59.95)
    item_2 = retail_item_class.RetailItem('Designer Jeans', 40, 34.95)
    item_3 = retail_item_class.RetailItem('shirt', 20, 24.95)

    #use the get methods to print the info of the items
    #to check the code
    # print(item_1.get_item_desc())
    # print(item_1.get_units())
    # print(item_1.get_price())
    # print()
    # print(item_2.get_item_desc())
    # print(item_2.get_units())
    # print(item_2.get_price())
    # print()
    # print(item_3.get_item_desc())
    # print(item_3.get_units())
    # print(item_3.get_price())

#run the main
main()



    
