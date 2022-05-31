#This program gives the user 2 random
#numbers to add and tells the user if
#their answer is correct

#import the random module for later use
import random

#define the main
def main():
    #describe the program to the user
    print('Hello, this is a math quiz')
    print('I will give you two numbers to add')

    #get two random numbers
    random_num_1 = random_num()
    random_num_2 = random_num()

    #ask the user to find the sum and store their answer
    user_answer = float(input(f'What is {random_num_1} + {random_num_2}?: '))

    #tell the user if they are correct or wrong
    if user_answer == sum(random_num_1, random_num_2):
        print('Congratulations! You are correct.')
    
    else:
        print('That is incorrect.', end = ' ')
        print(f'The correct answer is {sum(random_num_1, random_num_2)} ')

#define the random_num function
def random_num():
    return random.randint(0,1000)

#define the sum function
def sum(x,y):
    return x + y

#run the main
main()