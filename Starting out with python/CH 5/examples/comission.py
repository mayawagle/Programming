#this program canculates sales commissions
def main():
    #create a variabloe to control the loop
    keep_going = 'y'

    #calculate a series of commissions 
    while keep_going == 'y':
        #get a salesperson's sales and commission rate
        sales = float(input('Enter the amount of sales'))
        comm_rate = float(input('Enter the commission rate: '))

        #calculate the commission
        commission = sales * comm_rate

        #Display the commission
        print(f'The commission is ${format(commission, ".2f")}')

        #See if the user wants to do another one
        keep_going = input('Do you want to calculate another commission? (Enter y for yes): ')

#call the main
main()