#This program uses the return value of a function

def main():
    #get the user's age
    first_age = int(input('Enter your age: '))

    #Get tyhe user's best friend's age
    second_age = int(input("Enter your best friend's age: "))

    #Get the sum of both ages
    total = sum(first_age, second_age)

    #display the total age
    print(f'Together you are {total} years old.')

#THe sum function accepts two numeric arguments and
#returns the sum of those arguments

def sum(num1, num2):
    result = num1 + num2
    return result

#Call the main function
main()