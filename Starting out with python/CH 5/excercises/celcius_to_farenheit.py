#This program displays a table of celcius temperatures from 0-20
#and their farenheit equivalent

#define the constants
RANGE_TEMP_MIN = 0
RANGE_TEMP_MAX = 20

#define the main
def main():
    #print the table headings
    print()
    print("Celcius\tFarenheit")
    print('--------------------------')

    #Print the data
    for degree_celcius in range(RANGE_TEMP_MIN,RANGE_TEMP_MAX + 1):
        farenheit = (9/5) * degree_celcius + 32
         #format the data to the chart
        print(degree_celcius, '\t', format(farenheit, ".2f"))

#run the main
main()

