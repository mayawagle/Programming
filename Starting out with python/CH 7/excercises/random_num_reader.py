#This program reads the numbers from numbers.txt and displays the 
#numbers, total of the numbers and number of numbers

#define the main
def main():
    #open the file
    infile = open('random_nums.txt', 'r')

    #start accumulator variables
    total = 0
    numbers = 0

    #do a priming read
    num = infile.readline()
    num = num.rstrip('\n')
    total  += int(num)
    numbers = 0

    #initiate the while loop
    while num != "":
        num = num.rstrip('\n')
        print(num)
        total += int(num)
        numbers += 1
        num = infile.readline()
       

    #close the file
    infile.close()

    #print the total and number of numbers
    print(f'The total of the random numbers is {total}.')
    print(f'There are {numbers}')

#run the main
main()

    