replacement_cost = 0
#define the main
def main():
    #call the replacement
    get_replacement_cost()
    # call the calculate minimum insurance func
    calculate_minimum_insurance()

#define the get replacement cost func
def get_replacement_cost():
    global replacement_cost
    replacement_cost = float(input('Enter the replacement cost: '))

#define the minimum insurance func
def calculate_minimum_insurance():
    minimum_insurance = .80 * replacement_cost
    print(f'You should buy a minimum of ${format(minimum_insurance,".2f")} for insurance')

#call the main
main()
