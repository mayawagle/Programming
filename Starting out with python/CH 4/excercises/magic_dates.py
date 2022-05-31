#this program tells the user if the date is magic

#define the main
def main():
    #get information from the user
    month = int(input('Enter the month in numeric form: '))
    day = int(input('Enter the day of the month in numeric form: '))
    year = int(input('Enter a two digit year: '))

    #determine if the date is magic
    if month * day == year:
        print('The date is magic!')
    else:
        print('The date is not magic.')

#call the main
main()