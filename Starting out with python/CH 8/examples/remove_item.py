#This program demonstrates how to use the remove 
#method to remove an item from a lsit

def main():
    #create a list with some items
    food = ['Pizza', 'Burgers', 'Chips']

    #display the lsit
    print('Here are the items in the food list:')
    print(food)

    #Get the item to change
    item = input('Which item should I remove?')

    try:
        #remove the item
        food.remove(item)

        #display th list 
        print('Here is the revised list: ')
        print(food)

    except ValueError:
        print('That item was not found in the list.')

#call the main
main()
