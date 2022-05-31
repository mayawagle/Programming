#This program prompts the user for sales amounts
#and writes those amounts to the sales.txt file

def main():
    #Get the number of days
    num_days = int(input('for how many days do you have sales?'))

    #open a new file named sales.txt
    sales_file = open('sales.txt', 'w')

    #Get the amount of sales for each day and write 
    #it to the file
    for count in range(1, num_days + 1):
        #get the sales for a day
        sales = float(input(f'Enter the sales for day {count}: '))

        #write the sales amount to the file
        sales_file.write(str(sales) + '\n')

    #close the file
    sales_file.close()
    print('Data written to sales.txt')

#call the main
main()