#in this program, the computer generates a random number that the user has to guess
#the computer tells them if they are too high or low and congratulates them 
#when they get it right. It also tells the user their number of guesses

#import random module for number
import random
#define the main
def main():
    #initiate a variable to keep the game running and one to count guesses
    yes_or_no = 'yes'
    guesses = 0
    while yes_or_no == 'yes':
        number = random.randint(1,101)
        user_guess = int(input('Guess a number: '))
        while user_guess != number:
            print(too_high_or_low(number,user_guess))
            guesses += 1
            user_guess = int(input('Guess another number: '))

        print(f'Congratulations! You are correct. The number was {number}. It took you {guesses + 1} guesses.')
        yes_or_no = str(input('Would you like to play again?(type yes or no): '))

#define the too_high_or_low function
def too_high_or_low(number,guess):
    if guess < number:
        return 'Too low, try again'
    if guess > number:
        return 'Too high, try again'

#run the main
main()