#this program estimates the work and money needed for a paint job

#def globals
gallons_required = 0
cost_of_paint = 0
hours_of_labor = 0
labor_charges = 0
#define the main
def main():
    #get the square feet
    square_feet = float(input('What is the square feet of wall space to be painted?: '))
    price_per_gallon = float(input('What is the price per gallon of paint?: '))
    #call calculating functions
    calculate_gallons_required(square_feet)
    calculate_hours_of_labor(gallons_required)
    calculate_cost_of_paint(price_per_gallon,gallons_required)
    calculate_labor_charges(hours_of_labor)
    calculate_total_cost(cost_of_paint,labor_charges)

def calculate_gallons_required(square_feet):
    global gallons_required
    gallons_required = square_feet / 115
    print(f'{gallons_required} gallons of paint are required')

def calculate_cost_of_paint(price_per_gallon,gallons_required):
    global cost_of_paint
    cost_of_paint = price_per_gallon * gallons_required
    print(f'The cost of the paint is ${format(cost_of_paint,".2f")}')

def calculate_hours_of_labor(gallons_required):
    global hours_of_labor
    hours_of_labor = gallons_required * 8
    print(f'The paint job will require {format(hours_of_labor,".2f")} hours of labor')

def calculate_labor_charges(hours_of_labor):
   global labor_charges
   labor_charges = 20 * hours_of_labor
   print(f'The labor will cost ${format(labor_charges,".2f")}')

def calculate_total_cost(cost_of_paint,labor_charges):
    total_cost = cost_of_paint + labor_charges
    print(f'The total cost of the paint job is ${format(total_cost,".2f")}')

#call the main
main()