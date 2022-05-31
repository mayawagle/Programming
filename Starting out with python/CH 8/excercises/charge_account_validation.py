
def main():
    #open the file for reading
    infile = open('charge_accounts.txt', 'r')

    #read the contents of the list to a file
    account_numbers = infile.readlines()

    #close the file
    infile.close()

    #strip the newline character from each item in the list
    #make an initiator variable to control the loop
    index = 0
    while index < len(account_numbers):
        account_numbers[index] = account_numbers[index].rstrip('\n')
        index += 1

    #print cities to test program
    #print(account_numbers)

    #get the charge account number from the user
    test_number = int(input('Enter the account number: '))

    #check for the number
    for item in account_numbers:
        if int(item) == test_number:
            print('The number is valid.')
            return 

    print('The number is invalid.')
            

            
        
#run the main
main()