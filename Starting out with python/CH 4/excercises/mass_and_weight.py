#this program calculates an object's weight based on its mass
#It then tells the user if the item is too heavy

#define the main
def main():
    #get the mass 
    mass = float(input('Enter the mass in kilograms: '))
    #calculate the weight
    weight = mass * 9.8
    #determine/print if the object is too heavy
    if weight > 1000:
        print('The object is too heavy.')
    if weight < 10:
        print('The object is too light.')

#call the main
main()
