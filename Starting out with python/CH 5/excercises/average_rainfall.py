#This program takes in the rainfall per month over a certain period of time and calculates the average rainfall per month

#Define the main
def main():
    years = int(input('How many years are in your data set?: '))
    #set an accumulator variable for the total inches of rainfall
    total_rainfall_inches = 0

    #write the outer loop
    for year in range (1, years + 1):
        #write the inner loop
        for month in range(1,13):
            month_rainfall = float(input(f'What is the average rainfall for month {month} of year {year}?: '))

            #add to the accumulator
            total_rainfall_inches += month_rainfall
            

    #print the data
    months = 12 * years
    average_rainfall = total_rainfall_inches / months

    print(f'You entered data for a period of {months} months or {years} year(s).')
    print(f'Over the course of this time, there was a total of {total_rainfall_inches} inches of rainfall.')
    print(f'This means an average of {average_rainfall} inches fell per month')
#run the main
main()  