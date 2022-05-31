#This program generates 100 random numbers, and keeps a count of how many of those 
# random numbers are even and how many are odd.

#import random
import random

#define the main
def main():
    #initiate an accumulater variable 
    even = 0
    odd = 0
    for num in range(100):
        num = random.randint(1,1000) 
        if even_or_odd(num) == 'even':
            even += 1
        else:
            odd += 1
    print(f'There are {even} even numbers and {odd} odd numbers.')

#define the even_or_odd func
def even_or_odd(number):
    if number % 2 == 0:
        return 'even'
    else:
        return 'odd'


#run the main
main()