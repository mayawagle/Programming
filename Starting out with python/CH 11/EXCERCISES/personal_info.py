#March 23
# #Chapter 11 pg 479

#This program makes a personal information class that
##stores the attributes: name,adress,age,phone number
#it then creates 3 instances of the class

#define the class
class personal_information:
    def __init__(self, name, adress, age, number):
        self.__name = name
        self.__adress = adress
        self.__age = age
        self.__number = number

    #write the accessor and mutator methods
    def get_name(self):
        return self.__name

    def get_adress(self):
        return self.__adress

    def get_age(self):
        return self.__age

    def get_number(self):
        return self.__number

    def set_name(self,name):
        self.__name = name
    
    def set_adress(self,adress):
        self.__adress = adress
    
    def set_age(self, age):
        self.__age = age

    def set_number(self, number):
        self.__number = number

#define the main
def main():
    personal_information_maya = personal_information('maya','burlingame',18,650)
    personal_information_layla = personal_information('layla','san mateo',15,650)
    personal_information_ky = personal_information('ky','san mateo',15,650)

    print('Maya info:')
    print(personal_information_maya.get_name())
    print(personal_information_maya.get_adress())
    print(personal_information_maya.get_age())
    print(personal_information_maya.get_number())
    print()

    print('layla info:')
    print(personal_information_layla.get_name())
    print(personal_information_layla.get_adress())
    print(personal_information_layla.get_age())
    print(personal_information_layla.get_number())
    print()

    print('Ky info:')
    print(personal_information_ky.get_name())
    print(personal_information_ky.get_adress())
    print(personal_information_ky.get_age())
    print(personal_information_ky.get_number())

#run the main
main()