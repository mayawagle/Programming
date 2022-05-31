#this program generates a 7 digit lottery number
#and puts the numbers in a list
#it then prints the contents

#import the random module
import random

#define the constants
LEN_NUMBER = 7

#define the main
def main():
    print()
    #initiate a list
    lottery_number = []
    for num in range (1,LEN_NUMBER + 1):
        lottery_number.append(random.randint(0,9))
    #print the list
    for item in lottery_number:
        print(item)
    print()
    #the lottery number together is
    print('The lottery number is: ', end = "")
    for item in lottery_number:
        print(item, end = "")

#run the main
main()