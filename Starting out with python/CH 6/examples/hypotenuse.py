#This program calculates the length of a right 
#triangle's hypotenuse
import math

def main():
    #get the length of the triange's two sides
    a = float(input('Enter the length of side A: '))
    b = float(input('Enter the length of side B: '))

    #calculate the length of the hypotenuse
    c = math.hypot(a, b)

    #display the length of the hypotenuse
    print(f'The length of the hypotenuse is {c}')

#call the main
main()