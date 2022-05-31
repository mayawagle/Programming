#This program counts the number of bugs collected in a week

#define the main
def main():
    #define the while loop variable
    day = 0
    bugs = 0
    #write the while loop
    while day < 7:
        bugs = bugs + int(input('Enter the number of bugs collected today: '))

        #add 1 to the variabloe for the next day
        day +=  1
    #display number of bugs
    print(f'You have collected {bugs} bugs this week')


#call the main
main()


