#This porgram tells the user their time calculation

#define the main
def main():
    #get the seconds from the user 
    seconds = int(input('How many seconds do you want to calculate?: '))

    # Determine the calculation
    if seconds >= 60 and seconds< 3600:
        #determine the number of minutes
        minutes = seconds / 60
        print(f'The seconds translate to {format(minutes,".2f")} minutes')
    else:
        if seconds >= 3600 and seconds < 86400:
            #determine the number of hours
            hours = seconds / 3600
            print(f'The seconds translate to {format(hours,".2f")} hours')
        else:
            if seconds >= 86400:
                #determine the number of days
                days = seconds / 86400
                print(f'The seconds translate to {format(days,".2f")} days')

#call the main
main()
