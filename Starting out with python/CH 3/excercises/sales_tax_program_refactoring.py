#This program will calculate the total price of an item
#after the sales tax of the state and county

#Create global variables
subtotal = 0
state_tax = 0
county_tax = 0

#identify given info
STATE_TAX = .04
COUNTY_TAX = .02

#Write the main function
def main():
    #get the subtotal
    get_subtotal()
    #compute state tax
    compute_state_tax()
    #compute county tax
    compute_county_tax()
    #compute total purchase
    compute_total_purchase()

#define get subtotal function
def get_subtotal():
    global subtotal
    subtotal = float(input('What is the purchase before tax?: '))
    print(f'The purchase before tax is ${format(subtotal,".2f")} ')

#define the compute state tax function
def compute_state_tax(): 
    global state_tax
    state_tax = STATE_TAX * subtotal
    print(f'The state sales tax amounts to ${format(state_tax,".2f")}')

#define the compute county tax function
def compute_county_tax():
    global county_tax
    county_tax = COUNTY_TAX * subtotal
    print(f'The county sales tax amounts to ${format(county_tax,".2f")}')

#define the compute total purchase funciton
def compute_total_purchase():
    total_purchase = subtotal + county_tax + state_tax
    print(f'The total sale after tax is ${format(total_purchase,".2f")} ')

#call the main
main()