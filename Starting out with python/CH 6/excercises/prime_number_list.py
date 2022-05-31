#This program  displays all of the prime numbers from 1 through 100

#define the main
def main():
    for number in range(1,101):
        if is_prime(number) == True:
            print(number)


#copy is_prime function
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

#call the main
main()