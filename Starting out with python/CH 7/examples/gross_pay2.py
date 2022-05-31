#This program calculates gross pay

def main():
    try:
        #get the numbers of hours worked 
        hours = int(input('How many hours did you work? '))

        #get the hourly pay rate
        pay_rate = float(input('Enter your hourly pay rate: '))

        #calculate the gross pay
        gross_pay = hours * pay_rate

        #display the gross pay
        print(f'Gross pay: ${format(gross_pay, ",.2f")}, sep = ""')
    except ValueError:
        print('ERROR: Hours worked and hourly pay rate must be valid integers.')
        
#call the main
main()