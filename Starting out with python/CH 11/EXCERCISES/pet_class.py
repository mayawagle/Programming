#March 22
#Chapter 11 pg 479

#This program creates a class called pets holding the 
#the attributes: name, animal type and age. It then 
#prompts the user to enter the attributes for an instance
#it creates.

class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_type(self):    
        return self.__type

    def get_age(self):
        return self.__age

#define the main
def main():

    name = input('Enter the name of the animal: ')
    animal_type = input('Enter the type of animal the pet is: ')
    age = input('Enter the age of the pet: ')

    pet_1 = Pet(name,animal_type,age)

    print('The pet has the following data:')
    print(pet_1.get_name())
    print(pet_1.get_type())
    print(pet_1.get_age())

#run the main
main()


