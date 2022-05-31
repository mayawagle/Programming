#This program calculates sales commissions

def main():
    #Create a variable to control the loop
    keep_going = 'y'

    #calculate a series of commissions.
    while keep_going == 'y':
        #call the show_commission function
        #to display a salesperson's commission
        show_commission()

        #see if the user wants to do another one
        keep_going = input('Do you want to calculate another commission? (Enter y for yes): ')

#The show_commission function gets the amount of 
#sales and the commission rate, and then displays
#the amount of commission
def show_commission():
    #get a salesperson's sales and commission rate
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commission rate: '))

    #calculate the commision
    commission = sales * comm_rate

    #display the commission
    print(f'The commission is ${format(commission, ".2f")}') 

#call the main function
main()

