#This program calculates retail proces

#MARK_UP is used as a global constant for
#the markup up percentage

MARK_UP = 2.5

#The main funciton
def main():
    #variable to control the loop
    another = 'y'

    #Process one or more items
    while another == 'y' or another == 'Y':
        #Display an item's retail price.
        show_retail()

        #Do this again?
        another = input('Do you have another item?(enter y for yes): ')

# The show_retail function gets an item's wholesale
#cost and displays the item's retail price.
def show_retail():
    #Get the item's wholesale cost
    wholesale = float(input("enter the item's wholesale cost: "))

    #Calculate the retail price
    retail = wholesale * MARK_UP

    #Display the retail price
    print(f'Retail price: $ {format(retail,",.2f")} ')

#call the main
main()