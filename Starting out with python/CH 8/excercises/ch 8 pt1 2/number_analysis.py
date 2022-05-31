#this program asks the user to enter 20 numbers
#it stores the numbers in a list
#it then displays the min, max, total, average

#def the constants
NUMBERS = 3

#define the main
def main():
    #initiate a list
    numbers = []
    #get the numbers
    for num in range(1, NUMBERS + 1):
        numbers.append(float(input('Enter a number: ')))
    
    #find the min
    min = numbers[0]
    for item in numbers:
        if item < min:
            min = item

    #find the max
    max = numbers[0]
    for item in numbers:
        if item > max:
         max = item

    #find the total
    total = 0
    for item in numbers:
        total += item
    #use total to find average
    average = total / NUMBERS

    #print the data
    print(f'The min of the numbers is {min}')
    print()
    print(f'The max of the numbers is {max}')
    print()
    print(f'The total of the numbers is {total}')
    print()
    print(f'The average of the numbers is {format(average, ".2f")}')

#run the main
main()