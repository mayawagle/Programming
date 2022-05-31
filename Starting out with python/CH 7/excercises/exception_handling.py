#This program reads the numbers from numbers.txt and displays the 
#numbers, total of the numbers and number of numbers
#It handles an IOError and ValueError exceptions

#define the main
def main():
    #try to open the file
    try:
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

    #write the exceptions
    except IOError:
        print('The file does not exist or it is in', end = '')
        print('the incorrect location')
    
    except ValueError:
        print('An item read from the file cannot be converted to a number')

#run the main
main()