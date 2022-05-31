#This program calculates the total annual automobile cost


#define the main
def main():
    loan_payment = float(input('What is the monthly loan payment?'))
    insurance = float(input('What is the monthly insurance payment?'))
    gas = float(input('What is the monthly gas payment?'))
    oil = float(input('What is the monthly oil payment?'))
    tires = float(input('What is the monthly tires payment?'))
    maintenance = float(input('What is the monthly maintenance payment?'))
    #Print the monthly costs
    print(f'The monthly loan cost is ${format(loan_payment,".2f")}')
    print(f'The monthly cost of insurance is ${format(insurance,".2f")}')
    print(f'The monthly cost of gas is ${format(gas,".2f")}')
    print(f'The monthly cost of oil is ${format(oil,".2f")}')
    print(f'The monthly cost of tires is ${format(tires,".2f")}')
    print(f'The monthly cost of maintenance ${format(maintenance,".2f")}')
    #call total func
    annual_and_monthly_total(loan_payment,insurance,gas,oil,tires,maintenance)
#define the annual total func
def annual_and_monthly_total(val1,val2,val3,val4,val5,val6):
    collective_month = val1 + val2 + val3 + val4 + val5 + val6
    annual_total = collective_month * 12
    print(f'The monthly automobile cost is ${format(collective_month, ".2f")}')
    print(f'Your annual automobile cost is ${format(annual_total,".2f")}')
    
#call the main
main()
