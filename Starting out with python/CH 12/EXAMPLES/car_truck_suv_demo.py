#This program creates a Car object, a Truck object and 
#a SUV object

import vehicles
def main():
    #create a car object for a used 2001 BMW
    #with 70,000 miles, priced at 15,000 with
    #4 doors
    car = vehicles.Car('BMW', 2001, 7000, 15000.0, 4)

    #Create a truck object for a used 2002 
    #Toyota pickup with 40,000 miles, priced 
    #at 12,000 with 4-wheel drive
    truck = vehicles.Truck('Toyota', 2002, 40000, 12000.0, '4WD')

    #create an SUV object for a used 2000
    #volvo with 30,000 miles priced at 
    #18,500 with 5 passenger capacity
    suv = vehicles.SUV('Volvo', 2000, 30000, 18500.0, 5)

    print('Used Car Inventory')
    print('===================')

    #display the automobile data
    print('The following car is in inventory:')
    print(car)
    print()
    print('The following truck is in inventory:')
    print(truck)
    print()
    print('The following SUV is in inventory:')
    print(suv)
    print()

#call the main
main()

