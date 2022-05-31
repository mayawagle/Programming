#in this program, the user chooses a random number that the computer has to guess
#the user then tells the computer if its guess is too high or low 

#define the main
def main():
    #initiate a variable to keep the game going
    yes_or_no = 'yes'
    min = 0
    max = 101
    while yes_or_no == 'yes':
        #get a number from the user
        print('Choose a number between 1-100 for me to guess.')
        print('Got it? I am going to take a guess.')
        print()
        #guess a number
        feedback = 0
        while feedback != 'correct':
            comp_guess = half(min,max)
            #print guess and get feedback
            print(f'I guess {comp_guess}. ')
            feedback = input(('Am I too high, too low or correct? (print high, low, or correct): '))
            if feedback == 'high':
                max = comp_guess
            if feedback == 'low':
                min = comp_guess
            comp_guess == int(half(min,max))
        print('I got it! Good number.')
        yes_or_no = input("Would you like to play again? (type yes or no): ")
        min = 0
        max = 101
#define the half function
def half(min,max):
    return int((min + max) / 2)

#run the main
main()