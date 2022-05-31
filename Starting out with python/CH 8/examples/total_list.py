#this program calculates the total of the values 
#in a list

def main():
    #create a list
    numbers = [2,4,6,8,10]

    #create a variable to use as an accumulator
    total = 0

    #caculate the total of the list elements
    for value in numbers:
        total += value
    
    #display the total of the list elements
    print(f'The total of the elements is {total}')

#call the main
main()