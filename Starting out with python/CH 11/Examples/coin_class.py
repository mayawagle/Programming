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

#The main function
def main():
    #create an object from the coin class
    my_coin = Coin()

    #Display the side of the coin that is facing up
    print(f'This side is up: {my_coin.get_sideup()}')

    #Toss the coin
    print("I am tossing the coin...")
    my_coin.toss()

    #display the side of the coin that is facing up
    print(f'This side is up: {my_coin.get_sideup()}')

#call the main
main()