#This program demonstrates the BankAccount class

import bankaccount

def main():
    #get the starting balance
    start_bal = float(input('Enter your starting balance: '))

    #Create a Bankaccount object
    savings = bankaccount.BankAccount(start_bal)

    #deposit the user's paycheck
    pay = float(input('How much were you paid this week?'))
    print('I will deposit that into your account')
    savings.deposit(pay)

    #Display the balance
    print(f'Your account balance is ${format(savings.get_balance(), ".2f")}',sep= "")

    #Get the amount to withdraw
    cash = float(input('How much would you like to withdraw? '))
    print('I will withdraw that from your account.')
    savings.withdraw(cash)

    #display the balance
    print(f'Your account balance is ${format(savings.get_balance(), ".2f")}', sep= "" )

#call the main
main()