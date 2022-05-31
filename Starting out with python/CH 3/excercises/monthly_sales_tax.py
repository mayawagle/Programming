#This program calulates the amount of county,state and total sales tax
STATE_TAX = .04
COUNTY_TAX = .02

#def globals
county_tax = 0
state_tax = 0


def main():
    total_sales = float(input('Enter the total sales for the month: '))
    #call functions
    calculate_county_tax(total_sales)
    calculate_state_tax(total_sales)
    calculate_total_sales_tax(county_tax, state_tax)

#define the funcitons
def calculate_county_tax(total_sales):
    global county_tax
    county_tax = total_sales * COUNTY_TAX
    print(f'The county tax is ${format(county_tax, ".2f")}')

def calculate_state_tax(total_sales):
    global state_tax
    state_tax = total_sales * STATE_TAX
    print(f'The state tax is ${format(state_tax, ".2f")}') 

def calculate_total_sales_tax(county_tax, state_tax):
    total_sales_tax = county_tax + state_tax
    print(f'The total sales tax is ${format(total_sales_tax, ".2f")}')

#Call the main
main()