class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def deccelerate(self):
        self.__speed -= 5
        
    def get_speed(self):
        return self.__speed

def main():
    car1 = Car(2020, "Toyota")
    for i in range(5):
        car1.accelerate()
        print(f"Maya's car speed is {car1.get_speed()}")
    for i in range(5):
        car1.deccelerate()
        print(f"Maya's car speed is {car1.get_speed()}")
main()