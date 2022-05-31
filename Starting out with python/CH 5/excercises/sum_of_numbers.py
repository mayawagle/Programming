#This program takes in positive numbers entered by the user and then displays the
#sum of the given numbers

#define the main
def main():
    #tell the user what to do
    print('Enter your list of positive numbers. Enter a negative number', end = ' ')
    print('when you are done.')

    #set an accumulator variable to calculate the sum of the numbers
    sum = 0

    #ask for the first number
    number = float(input('Enter a number: '))

    #Write the while loop
    while number >= 0:
        sum += number
        #ask the user to enter another number
        number = float(input('Enter another number: '))
    
    #print the sum
    print(f'The sum of the numbers entered is {sum}.')
#run the main
main()