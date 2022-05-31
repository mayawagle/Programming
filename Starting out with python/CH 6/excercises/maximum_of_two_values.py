#This program uses the maximum function to tell the user which
#of the two numbers they enter is greater

def main():
    #get 2 numbers from user
    int1 = int(input('Enter an integer: '))
    int2 = int(input('Enter a second integer: '))

    print(f'The greater number is {maximum(int1, int2)}.')


#def maximum function
def maximum(int1, int2):
    if int1 > int2:
        return int1
    elif int1 < int2:
        return int2
    else:
        return 'Error'

#run the main
main()