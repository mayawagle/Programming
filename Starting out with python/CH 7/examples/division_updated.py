#This program divides a number by another number

def main():
    #get two numbers
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))

    #if num2 is not 0 divide and display
    if num2 != 0:
        #divide num1 by num2 and display the result
        result = num1 / num2
        print(f'{num1} divided by {num2} is {result}')
    else:
        print('Cannot divide by zero.')

#call the main
main()