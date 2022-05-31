#This program gets a store's sales for each day of the week
#it stores the amounts in a list then uses a loop to calculate the total sales

#def constants
DAYS_OF_WEEK = 7

#define the main
def main():
    #write an initial list
    sales_list = []
    total = 0
    #write a loop to get the data
    for day in range(1,DAYS_OF_WEEK + 1):
        sales_list.append(float(input(f'Enter the sales for day {day}: ')))

    #write a loop to run through sales_list and calculate the total
    for sale in sales_list:
        total += sale

    #print the total
    print(f'The total sales is ${format(total, ".2f")}.')

#run the main
main()