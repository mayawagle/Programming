import random

#The coin class simulates a coin that can be flipped


class Coin:

    #The __init__ method initializes the
    #sideup data attribute with heads

    #ex 11-4 ex change made (__)
    def __init__(self):
        self.__sideup = 'Heads'
    
    #The toss method generates a random number
    #in the range of 0-1. If the number is 0, the sideup
    #is set to 'Heads'. Otherwise the side up is set
    #to 'Tails'

    def toss(self):
        if random.randint(0,1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'
    
    #The get_sideup method returns the value 
    #referenced by sideup.

    def get_sideup(self):
        return self.__sideup