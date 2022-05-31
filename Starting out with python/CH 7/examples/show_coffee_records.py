#This program displays the records in the coffee.txt file
from pydoc import describe

def main():
    #open the coffee.txt file
    coffee_file = open('coffee.txt', "r")

    #read the first record's description field
    descr = coffee_file.readline()

    #read the rest of the file
    while descr != "":
        #read the quantitiy field
        qty = float(coffee_file.readline())

        #strip the \n from the description
        descr = descr.rstrip('\n')

        #display the record
        print(f'Description: {descr}')
        print(f'Quantity: {qty}')

        #read the next description
        descr = coffee_file.readline()
    
    #close the file
    coffee_file.close()

#call the main
main()