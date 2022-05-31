#This program writes a series of random numbers 1-100 to a file
#called random_nums.txt the user specifies how many numbers

#import random module
import random

#define the main
def main():
    #open a file
    outfile = open('random_nums.txt', 'w')

    #get the amount of numbers from the user
    how_many = int(input('How many numbers would you like?: '))

    #generate random numbers and write to file
    for num in range(0,how_many):
        random_int = random.randint(0,101)
        outfile.write(f'{str(random_int)}\n')
    
    #close the file
    outfile.close()

    print(f'{how_many} random numbers have been written to a file.')

#run the main
main()