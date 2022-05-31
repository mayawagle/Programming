#May 3, 2022
#Pg 487 12-1

#The automobile class holds genera; data 
#about an automobile in inventory

class Automobile:
    #the __init__method accepts arguments for the
    #make, model, mileage, and price. It initializes
    #the data attributes with these values

    def __init__(self,make,model,mielage,price):
        self.__make = make
        self.__model = model
        self.__mileage = mielage
        self.__price = price

    #The following methods are mutators for the 
    #class's data attributes

    def set_make(self, make):
        self.__make = make
    
    def set_model(self, model):
        self.__model = model
    
    def set_mileage(self,mileage):
        self.__mileage = mileage

    def set_price(self, price):
        self.__price = price

    #The following methods are the accessors 
    # for the class's data attributes

    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_mileage(self):
        return self.__mileage
    
    def get_price(self):
        return self.__price

    #the __str__ method returns a string of all the object's information
    def __str__(self):
        return (f"""Make: {self.__make}
Model: {self.__model}
Mileage: {self.__mileage}
Price ${self.__price}""")

#The car class represents a car. It is a subclass of 
#the automobile class

class Car(Automobile):
    #the __init__ method accepts arguments for the cars
    #make, model, mileage, price and doors

    def __init__(self, make, model, mileage, price, doors):
        #call the superclass's __init__ method and pass
        #the required arguments. Also need self
        Automobile.__init__(self, make, model, mileage, price)

        #initialize the cars __doors attribute
        self.__doors = doors

    #the set doors method is a mutator for the attribute
    def set_doors(self, doors):
        self.__doors = doors
    
    #the get doors method is an accessor for the doors attribute
    def get_doors(self):
        return self.__doors

    #write the str method
    def __str__(self):
        return super().__str__() + f"\nDoor: {self.__doors}"

#Te truck class represents a pick up truck. It is a subclass
#o the automobile class
class Truck(Automobile):
     #the __init__ method accepts arguments for the 
     #Trucks make, model, mileage, price and drive type
     def __init__(self, make, model, mileage, price, drive_type):
         #call the superclass init method and pass
         #the required arguments and self
         Automobile.__init__(self, make, model, mileage, price)
         #initialize the __drive_type attribute
         self.__drive_type = drive_type
     #the set_drive_type method is the mutator for 
     #the drive_type attribute
     def set_drive_type(self, drive_type):
         self.__drive = drive_type
     
     #the get_drive_type method is the accessor fort the
     #__drive_type attribute
     def get_drive_type(self):
         return self.__drive_type

#Te SUV class represents a sport utility vehicle. it is a 
#subclass of the Automobile class

class SUV(Automobile):
    #the __init__ method accepts arguments for the 
    #SUV make, model, mileage, price and passenger capacity

    def __init__(self, make, model, mileage, price, pass_cap):
        #call the superclass __init__ method and pass 
        #the required arguments and self
        Automobile.__init__(self,make,model,mileage,price )
        
        #Initialize the __pass_cap attribute
        self.__pass_cap = pass_cap
    
    #the set_pass_cap method is the mutator for the __pass_cap attribute

    def set_pass_cap(self,pass_cap):
        self.__pass_cap = pass_cap
    
    def get_pass_cap(self):
        return self.__pass_cap

class EV(Automobile):
    #the __init__ methos accepts arguments for the
    #EV make, model, mileage, price, battery info

    def __init__(self, make, model, mileage, price, charge):
        #call the superclass __init__method
        Automobile.__init__(self,make,model,mileage,price)

        #initialize the __charge attribute
        self.__charge = charge
    
    #The set charge method is the mutator for the __charge attribute
    def set_charge(self, charge):
        self.__charge = charge
    
    def get_charge(self):
        return self.__charge
