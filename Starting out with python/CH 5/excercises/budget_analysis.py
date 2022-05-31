#This program tells the user if they anre over
#or under budget for the month

#define the main
def main():
    #get the amount budgeted for the month
    budget = float(input('Enter the amount budgeted for this month: '))

    #initialize an accuulator variable
    total_spent = 0

    #create a variable to control the loop
    keep_going = 'y'

    #write the loop
    while keep_going == "y" or keep_going == 'Y':
        total_spent += float(input('Enter an expense for the month: '))

        keep_going = input('Are there more expenses? (enter y for yes and n for no)')



    #Print the results
    if total_spent == budget:
        print("You have reached your budget exactly.")
    
    if total_spent < budget:
        under_budget_amount = budget - total_spent
        print(f'You are ${under_budget_amount} under budget')

    if total_spent > budget:
        over_budget_amount = total_spent - budget
        print(f'You are ${over_budget_amount} over the budget')

#run the main
main()
