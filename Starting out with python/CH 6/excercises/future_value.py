#This program takes in the present value and monthly interest
#rate and returns the value of the account based on the 
#amount of months the user enters

#define the main

def main():
    #get the values
    present_value = float(input('What is the current balance of the account?: '))
    monthly_rate = float(input('What is the monthly interest rate of the account?: '))
    number_months = float(input('How many months will the money be left in the account?: '))

    #call the future_value function
    print(f'In {number_months} months, there will be ${format(future_value(present_value,monthly_rate,number_months), ".2f")} in the account')


#define the future_value function
def future_value(p,i,t):
    return p * (1 + i)**2
    
#run the main
main()