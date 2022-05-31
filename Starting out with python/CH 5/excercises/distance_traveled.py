#This program tells the user the distance traveled each hour

#define the main
def main():
    #Get the speed of the vehicle
    speed = int(input('Enter the speed in mph: '))

    #Get the hours traveled
    time = int(input('Enter the hours traveled: '))

    #print the table headings
    print()
    print("Hour\tDistance Traveled")
    print('--------------------------')

    #write the for loop for each hour
    for hour in range(1,time + 1):
        distance_traveled = hour * speed

        #format the data to the chart
        print(hour, '\t', distance_traveled)






#call the main
main()