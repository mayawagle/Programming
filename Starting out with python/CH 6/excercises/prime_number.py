#this program takes in an integer and prints true if the 
# integer is prime and false if it is not

#define the main
def main():
    integer = int(input('Enter a number: '))
    if is_prime(integer) == True:
        print(f'The number {integer} is a prime number.')
    else:
        print(f'The number {integer} is not prime.')

#define the is_prime function
def is_prime(integer):
    if integer < 5:
        for num in range(2, int(integer)):
            if integer%num == 0:
                return False
        return True
    else:
        for num in range(2, int(integer/2)):
            if integer%num == 0:
                return False
        return True

#run the main
main()

