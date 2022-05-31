#This program allows the user to play rock paper scissors against the computer

#import the random module
import random

#define the main
def main():
    #generate a variable to keep the game running
    yes_or_no = 'yes'
    while yes_or_no == 'yes':
        comp_choice = object_choice(random.randint(1,4))
        user_choice = str(input('Enter rock, paper, or scissors: '))
        print(f'I chose {comp_choice}. ')
        
        if user_choice == comp_choice: 
            print('lets play again to determine the winner')
        else:
            if who_won(comp_choice, user_choice) == 'computer':
                print(f'I won. {comp_choice} beats {user_choice}')
            else:
                print(f'You won. {user_choice} beats {comp_choice}')
            yes_or_no = str(input('Whould you like to play again (type yes or no): '))

        
#define the object_choice function
def object_choice(num):
    if num == 1:
        return 'rock'
    elif num == 2:
        return 'paper'
    else:
        return 'scissors'

#define the who_won function
def who_won(comp_choice, user_choice):
    if comp_choice == 'rock' and user_choice == 'paper':
        return 'user'
    elif comp_choice == 'rock' and user_choice == 'scissors':
        return 'computer'
    elif comp_choice == 'scissors' and user_choice == 'paper':
        return 'computer'
    elif comp_choice == 'scissors' and user_choice == 'rock':
        return 'user'
    elif comp_choice == 'paper' and user_choice == 'rock':
        return 'computer'
    elif comp_choice == 'paper' and user_choice == 'scissors':
        return 'user'


#run the main
main()