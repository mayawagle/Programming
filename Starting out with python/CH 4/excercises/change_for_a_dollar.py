#This program determines if the numbers opf coins are 
#equal to, greater, or less than a dollar

#define the constants
PENNY = 1
NICKEL = 5
DIME = 10
QUARTER = 25
DOLLAR = 100

#Define the main
def main():
    #get the user input for amount of coins
    pennies_entered = int(input('Enter the number of pennies: '))
    nickels_entered = int(input('Enter the number of nickels: '))
    dimes_entered = int(input('Enter the number of dimes: '))
    quarters_entered = int(input('Enter the number of quarter: '))

    #calculate the sum of money
    total = (pennies_entered * PENNY) + (nickels_entered * NICKEL) + (dimes_entered * DIME) + (quarters_entered * QUARTER)

    #write if statements to determine if coins make a dollar
    if total == DOLLAR:
        print('Congratulations! You made a dollar!')
    if total < DOLLAR:
        print('Your total was less than a dollar. Try again.')
    if total > DOLLAR:
        print('Your total was more than a dollar. Try again.')

#run the main
main()



