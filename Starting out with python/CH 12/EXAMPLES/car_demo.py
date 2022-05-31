#this program demonstrates the car class

from enum import auto
import vehicles

def main():
    #create an object from the car class
    used_car = vehicles.Car('Audi', 2007, 12500, 21500.00, 4)

    #display the car's data
    print(f'Make: {used_car.get_make()}')
    print(f'Model: {used_car.get_model()}')
    print(f'Mileage: {used_car.get_mileage()}')
    print(f'Price: {used_car.get_price()}')
    print(f'Number of doors: {used_car.get_doors()}')

    #create a new object
    automobile_1 = vehicles.Automobile('Toyota', 'Tacoma', 12500, 6000)
    print(automobile_1)

    #create a car
    car_1 = vehicles.Car('Audi', 2009, 125, 215000.00, 2)
    print(car_1)

    #create autos list
    autos = []
    autos.append(used_car)
    autos.append(automobile_1)
    autos.append(car_1)

    for automobile in autos:
        print(automobile)
        print()
#call the main function
main()