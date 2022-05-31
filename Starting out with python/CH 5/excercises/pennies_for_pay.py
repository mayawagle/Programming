#This program calculates the amount of money a person makes per day and in total
#if they are paid in pennies and their wage doubles each day.

#define the main
def main():
    #get the number of days
    days = int(input('How many days have you worked?: '))

    #set an accumulator variable to calculate the pennies earned
    pennies_earned = 0

    # #print the table headings
    print()
    print("days\tPennies earned")
    print('--------------------------')


    #write the for loop
    for day in range(1,days + 1):
        pennies_earned_on_day = 2 ** (day - 1)
        pennies_earned += pennies_earned_on_day

        
        #fill the table with the pennies earned data
        print(f'day {day}\t\t{pennies_earned_on_day}')

    #Tell the user the total pay for the end of the period
    total_dollars = pennies_earned / 100
    print(f'The total pay is ${total_dollars}.')

#run the main
main()