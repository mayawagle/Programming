#This program allows the user to search the
#coffww.txt file for records matching a description

def main():
    #create a bool variable to use as a flag
    found = False

    #Get the search value
    search = input('Enter a description to search for: ')

    #open the coffee.txt file
    coffee_file = open('coffee.txt', 'r')

    #read the first record's description field
    descr = coffee_file.readline()

    #read the rest of the file
    while descr != "":
        #read the quantity field
        qty = float(coffee_file.readline())

        #strip the \n from the description
        descr = descr.rstrip('\n')

        #determine whether this record matches
        #the search value
        if descr == search:
            #display the record
            print(f'Description: {descr} ')
            print(f'Quantity: {qty}')
            print()
            #set the found flag to True
            found = True
        
        #read the next description
        descr = coffee_file.readline()
    
    #close the file
    coffee_file.close()
    
    #If the search value was not found in the file
    #display a message
    if not found:
        print('That item was not found on the file.')

#runt the main
main()