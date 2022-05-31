#This program demonstates an infinite loop
def main():
    #create a variable to control the loop
    keep_going = 'y'

    #Warning! Infinite loop!
    while keep_going == 'y':
         #get a salesperson's sales and commission rte
        sales = float(input('Enter the amount of sales: '))
        comm_rate = float(input('Enter the commission rate: '))

    #Calculate the commission
    commission = sales * comm_rate

    #Display the commission
    print(f'The commission is ${format(commission, ".2f")}')

#call the main
main()