#This program asks the user for the calories burned between 10 and 30 
#minutes in 5 minute increments

#Define the constants
CALS_PER_MIN = 3.9
#define the main
def main():
    #write the for loop 
    for minutes in range (10,35,5):
        calories_burned = minutes * CALS_PER_MIN
        print(f'You have burned {calories_burned} calories in {minutes} minutes')
    
#call the main
main()
